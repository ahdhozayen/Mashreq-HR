from django.db import models
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Department(models.Model):
    dept_name	=	models.CharField(max_length=150,verbose_name=_('Department'))
    start_date	=	models.DateField(auto_now=False, auto_now_add=False, default=date.today,verbose_name=_('Start  Date'))
    end_date	=	models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,verbose_name=_('End Date'))
    created_by =    models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="department_created_by")
    creation_date	=	models.DateField(auto_now=True, auto_now_add=False)
    last_update_by	=	models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="department_last_update_by")
    last_update_date	=	models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.dept_name

class Job(models.Model):
    job_name	=	models.CharField(max_length=100,verbose_name=_('Name'))
    job_description = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('Description'))
    start_date	=	models.DateField(auto_now=False, auto_now_add=False, default=date.today,verbose_name=_('Start Date'))
    end_date	=	models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,verbose_name=_('End Date'))
    created_by =    models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="job_created_by")
    creation_date	=	models.DateField(auto_now=True, auto_now_add=False)
    last_update_by	=	models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="job_last_update_by")
    last_update_date	=	models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.job_name

class Position(models.Model):
    job	=	models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True, related_name='position_job_fk',verbose_name=_('Job'))
    department	=	models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True, related_name='position_dept_fk',verbose_name=_('Department'))
    position_name	=	models.CharField(max_length=150,verbose_name=_('Position'))
    position_description = models.CharField(max_length=255, null=True, blank=True,verbose_name=_('Position Description'))
    start_date	=	models.DateField(auto_now=False, auto_now_add=False, default=date.today,verbose_name=_('Start Date'))
    end_date	=	models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,verbose_name=_('End Date'))
    created_by =    models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="position_created_by")
    creation_date	=	models.DateField(auto_now=True, auto_now_add=False)
    last_update_by	=	models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="position_last_update_by")
    last_update_date	=	models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.position_name
