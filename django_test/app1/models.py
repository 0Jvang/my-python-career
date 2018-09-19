from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    # verbose_name = 'user'
    account = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'id:{self.id},account:{self.account},passwd:{self.password}'



