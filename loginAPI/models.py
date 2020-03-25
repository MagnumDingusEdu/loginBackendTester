from django.db import models

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=100, default='' )
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    access_token = models.CharField(max_length=100, default='', blank=True)
    loggedin = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    