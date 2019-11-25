from django.contrib import admin
from django.contrib.auth.models import Group
from employee.models import Employee, Job_Roll, Employee_Attachment, Employee_Leaves
from definition.models import LookupDet


admin.site.site_header= 'Mashreq Arabia HR System'
admin.site.unregister(Group)

class JobRollInlineAdmin(admin.TabularInline):
    fields = (
        'emp_id',
        'manager',
        'position',
        'leaves_deserved',
        'salary',
        'reason_of_leaving',
        'start_date',
        'end_date',
    )
    model = Job_Roll
    fk_name = 'emp_id'

class EmployeeAttachmentInlineAdmin(admin.TabularInline):
    fields = (
        'emp_id',
        'attachment_name',
        'attachment',
        'start_date',
        'end_date',
    )
    model = Employee_Attachment
####################################################################
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_number', 'emp_name', 'hiredate')
    list_filter = ('emp_name',)
    fields =(
        'emp_number',
        'emp_name',
        'address1',
        'phone',
        'mobile',
        'date_of_birth',
        'hiredate',
        'email',
        'picture',
        'identification_type',
        'id_number',
        'place_of_birth',
        'nationality',
        'field_of_study',
        'education_degree',
        'gender',
        'social_status',
        'military_status',
        'religion',
        'insured',
        'insurance_number',
        'insurance_date',
        'has_medical',
        'medical_number',
        'medical_date',
        'start_date',
        'end_date',
    )
    inlines =[
        JobRollInlineAdmin,
        EmployeeAttachmentInlineAdmin
    ]
    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['gender'].queryset = LookupDet.objects.filter(lookup_type_fk__lookup_type_name__iexact='GENDER')
         context['adminform'].form.fields['identification_type'].queryset = LookupDet.objects.filter(lookup_type_fk__lookup_type_name__iexact='IDENTITY_TYPE')
         context['adminform'].form.fields['social_status'].queryset = LookupDet.objects.filter(lookup_type_fk__lookup_type_name__iexact='SOCIAL_STATUS')
         context['adminform'].form.fields['religion'].queryset = LookupDet.objects.filter(lookup_type_fk__lookup_type_name__iexact='RELIGION')
         context['adminform'].form.fields['military_status'].queryset = LookupDet.objects.filter(lookup_type_fk__lookup_type_name__iexact='MILITARY_STATUS')
         return super(EmployeeAdmin, self).render_change_form(request, context, *args, **kwargs)
     # save the TabularInline data
    def save_formset(self, request, form, formset, change):
     instances = formset.save(commit=False)
     for instance in instances:
         instance.created_by = request.user
         instance.last_update_by = request.user
         instance.save()
         formset.save_m2m()
     # save the ModelAdmin data here
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
            instance.last_update_by = user
            instance.save()
            form.save_m2m()

@admin.register(Employee_Leaves)
class EmployeeLeavesAdmin(admin.ModelAdmin):
    fields =(
        'emp_id',
        'leave_type',
        'abscent_days',
        'reason',
        'leave_balance',
        'start_date',
        'end_date',
    )
    readonly_fields =['leave_balance', 'abscent_days',]
    list_display = ('emp_id', 'leave_balance','start_date','end_date',)
    list_filter = ('emp_id',)

    def render_change_form(self, request, context, *args, **kwargs):
         context['adminform'].form.fields['leave_type'].queryset = LookupDet.objects.filter(lookup_type_fk__lookup_type_name__iexact='LEAVE_TYPE')
         return super(EmployeeLeavesAdmin, self).render_change_form(request, context, *args, **kwargs)
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
            instance.last_update_by = user
            instance.save()
            form.save_m2m()
