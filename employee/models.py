from django.db import models
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from definition.models import LookupType, LookupDet
from company.models import (Department, Position, Job)

class Employee(models.Model):
    emp_number = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Employee Number'))
    emp_name = models.CharField(max_length=60, verbose_name=_('Employee Name'))
    address1 = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('address1'))
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('phone'))
    mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('mobile'))
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name=_('Birthdate'))
    hiredate = models.DateField(auto_now=False, auto_now_add=False, default=date.today, verbose_name=_('Hire Date'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('email'))
    picture = models.ImageField(null=True, blank=True, verbose_name=_('picture'))
    identification_type	= 	models.ForeignKey(LookupDet, on_delete=models.CASCADE, null=True, blank=True, related_name='employee_id_type', verbose_name=_('ID Type'))
    id_number = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('ID Number'))
    place_of_birth = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Place of Birth'))
    nationality = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Nationality'))
    field_of_study = models.CharField(max_length=30, blank=True, null=True, verbose_name=_('Field of Study'))
    education_degree = models.CharField(max_length=30, blank=True, null=True, verbose_name=_('Eductaion Degree'))
    gender = models.ForeignKey(LookupDet, on_delete=models.CASCADE, null=True, blank=True, related_name='gender_list', verbose_name=_('Gender'))
    social_status	= 	models.ForeignKey(LookupDet, on_delete=models.CASCADE, null=True, blank=True, related_name='employee_social', verbose_name=_('Social Status'))
    military_status	= 	models.ForeignKey(LookupDet, on_delete=models.CASCADE, null=True, blank=True, related_name='employee_military', verbose_name=_('Milatery Status'))
    religion	= 	models.ForeignKey(LookupDet, on_delete=models.CASCADE, null=True, blank=True, related_name='employee_religion', verbose_name=_('Religion'))
    insured = models.BooleanField(verbose_name=_('Insured'))
    insurance_number = models.CharField(max_length=30, blank=True, null=True, verbose_name=_('Insurance Number'))
    insurance_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name=_('Insurance Date'))
    has_medical = models.BooleanField(verbose_name=_('Has Medical'))
    medical_number = models.CharField(max_length=30, blank=True, null=True, verbose_name=_('Medical Number'))
    medical_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name=_('Medical Date'))
    start_date = models.DateField(auto_now=False, auto_now_add=False, default=date.today, verbose_name=_('Start Date'))
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name=_('End Date'))
    created_by = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="emp_created_by")
    creation_date = models.DateField(auto_now=True, auto_now_add=False)
    last_update_by = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    last_update_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.emp_name

class Job_Roll(models.Model):
    emp_id      = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True, blank=True, related_name='job_roll_emp', verbose_name=_('Employee'))
    manager     = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True,  related_name='job_roll_manager', verbose_name=_('Manager'))
    position    = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Position'))
    leaves_deserved = models.PositiveIntegerField(validators=[MaxValueValidator(52), MinValueValidator(0)])
    salary  =  models.FloatField(default=0.0, null=True, blank=True)
    reason_of_leaving = models.CharField(max_length=255, blank=True, null=True)
    start_date  = models.DateField(auto_now=False, auto_now_add=False, default=date.today, verbose_name=_('Start Date'))
    end_date    = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name=_('End Date'))
    created_by  = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="jobRoll_created_by")
    creation_date = models.DateField(auto_now=True, auto_now_add=False)
    last_update_by = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="jobroll_last_updated_by")
    last_update_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.position.position_name

class Employee_Attachment(models.Model):
    emp_id      = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True, blank=True, related_name='attach_emp', verbose_name=_('Employee'))
    attachment_name = models.CharField(max_length=150, verbose_name=_('Attachment Name'))
    attachment = models.ImageField(null=True, blank=True, verbose_name=_('Attachment'))
    start_date  = models.DateField(auto_now=False, auto_now_add=False, default=date.today, verbose_name=_('Start Date'))
    end_date    = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name=_('End Date'))
    created_by  = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="emp_attach_created_by")
    creation_date = models.DateField(auto_now=True, auto_now_add=False)
    last_update_by = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="emp_attach_last_updated_by")
    last_update_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.attachment_name

class Employee_Leaves(models.Model):
    emp_id      = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True, blank=True, related_name='leaves_emp', verbose_name=_('Employee'))
    leave_type =    models.ForeignKey(LookupDet, on_delete=models.CASCADE, null=True, blank=True, related_name='employee_leave_type', verbose_name=_('Leave Type'))
    abscent_days = models.PositiveIntegerField(validators=[MaxValueValidator(52), MinValueValidator(0)])
    reason = models.CharField(max_length=150, verbose_name=_('Leave Reason'))
    leave_balance = models.PositiveIntegerField(validators=[MaxValueValidator(52), MinValueValidator(0)])
    start_date  = models.DateField(auto_now=False, auto_now_add=False, default=date.today, verbose_name=_('Start Date'))
    end_date    = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name=_('End Date'))
    created_by  = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="emp_leaves_created_by")
    creation_date = models.DateField(auto_now=True, auto_now_add=False)
    last_update_by = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="emp_leaves_last_updated_by")
    last_update_date = models.DateField(auto_now=False, auto_now_add=True)

    def delete(self, *args, **kwargs):
        leavs_stock = Job_Roll.objects.get(emp_id=self.emp_id, end_date__isnull=True)
        leavs_stock.leaves_deserved = leavs_stock.leaves_deserved +  self.abscent_days
        self.leave_balance = self.leave_balance +  self.abscent_days
        super(Team, self).delete(*args, **kwargs)

    def save(self):
        leavs_stock = Job_Roll.objects.get(emp_id=self.emp_id, end_date__isnull=True)
        num_of_days = 0
        for x in Employee_Leaves.objects.filter(emp_id=self.emp_id):
            num_of_days = num_of_days + x.abscent_days
        self.abscent_days = (self.end_date-self.start_date).days + 1
        self.leave_balance = leavs_stock.leaves_deserved - ((num_of_days+(self.start_date-self.end_date).days + 1))
        super().save()

    def __str__(self):
        return self.emp_id.emp_name
