from django.db import models

# Create your models here.
class APKFile(models.Model):
	apkfile = models.FileField()