from django.db import models
#from django.contrib.postgres.fields import JSONField
#from django.utils.translation import gettext_lazy as _
from jsonfield import JSONField



# Create your models here.

class Countries(models.Model):
    data = JSONField(verbose_name="data")
    iso2 = models.CharField(verbose_name="iso2", max_length=3,null=True)
    error= models.BooleanField(verbose_name="error",default=False)
    msg = models.CharField(verbose_name="msg", max_length=100)
    name = models.CharField(verbose_name="name", max_length=100)
    capital = models.CharField(verbose_name="capital", max_length=100)
    iso3 = models.CharField(verbose_name="iso3", max_length=3)


    

