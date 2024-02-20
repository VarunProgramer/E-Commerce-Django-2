from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
def getfilename(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time, filename)
    return os.path.join('uploads/', new_filename)

class codegery(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    codegery_image = models.ImageField(upload_to=getfilename, null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class prodect(models.Model):
    codegery_type = models.ForeignKey(codegery,on_delete=models.CASCADE)
    Prodect_oner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=None)
    description = models.TextField(max_length=500)
    prodect_image = models.ImageField(upload_to=getfilename, null = True, blank=True)
    more_prodect_image = models.ImageField(upload_to=getfilename, null = True, blank=True)
    Uploadet_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name