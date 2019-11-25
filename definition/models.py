from django.db import models
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class LookupType(models.Model):
    lookup_type_name	=	models.CharField(max_length=100,verbose_name=_('Lookup Type'))
    lookup_type_description	=	models.CharField(max_length=255, null=True, blank=True,verbose_name=_('Description'))
    start_date	=	models.DateField(auto_now=False, auto_now_add=False, default=date.today,blank=True, null=True ,verbose_name=_('Start Date'))
    end_date	=	models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,verbose_name=_('End Date'))
    created_by =    models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="lookup_type_created_by")
    creation_date	=	models.DateField(auto_now=True, auto_now_add=False)
    last_update_by	=	models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="lookup_type_last_update_by")
    last_update_date	=	models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.lookup_type_name

class LookupDet(models.Model):
    lookup_type_fk	=	models.ForeignKey(LookupType, on_delete=models.CASCADE,related_name='lookup_type_fk',verbose_name=_('Lookup Type'))
    name	=	models.CharField(max_length=50,verbose_name=_('Name'))
    code	=	models.CharField(max_length=50,verbose_name=_('Code'))
    description	=	models.CharField(max_length=255, null=True, blank=True,verbose_name=_('Description'))
    start_date	=	models.DateField(auto_now=False, auto_now_add=False, default=date.today,verbose_name=_('Start Date') )
    end_date	=	models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,verbose_name=_('End Date'))
    created_by =    models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="lookup_det_created_by")
    creation_date	=	models.DateField(auto_now=True, auto_now_add=False)
    last_update_by	=	models.ForeignKey(User, blank=False,on_delete=models.CASCADE,related_name="lookup_det_last_update_by")
    last_update_date	=	models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
