from django.contrib import admin
from definition.models import LookupDet, LookupType

class LookupDetInline(admin.TabularInline):
    model = LookupDet
    fields = (
        'lookup_type_fk',
        'name',
        'code',
        'description',
        'start_date',
        'end_date',
    )


####################################### Admin Forms #############################################
@admin.register(LookupType)
class LookupTypeAdmin(admin.ModelAdmin):
    fields = (
            'lookup_type_name',
            'lookup_type_description',
            'start_date',
            'end_date',
    )
    inlines=[
        LookupDetInline,
    ]
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
