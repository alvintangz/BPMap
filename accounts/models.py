from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)