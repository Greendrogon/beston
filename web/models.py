from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField() 
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,
    models.SET_NULL,
    blank=True,
    null=True,)  # har user be yek Expense vasl mishe