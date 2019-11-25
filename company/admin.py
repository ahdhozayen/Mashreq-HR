from django.contrib import admin
from company.models import Department, Job, Position

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = (
        'dept_name',
        'start_date',
        'end_date',
    )
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.last_update_by = user
        instance.save()
        form.save()
        return instance

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = (
        'job_name',
        'job_description',
        'start_date',
        'end_date',
    )
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.last_update_by = user
        instance.save()
        form.save()
        return instance

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    fields = (
            'job',
            'department',
            'position_name',
            'position_description',
            'start_date',
            'end_date',
    )
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.last_update_by = user
        instance.save()
        form.save()
        return instance
