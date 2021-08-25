from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    '''
        Our UserProfile model extends the built-in Django User Model
        '''
    first_name = models.CharField(
        verbose_name="FirstName", max_length=320, null=False)
    last_name = models.CharField(
        verbose_name="LastName", max_length=320, null=False)
    country = models.IntegerField(verbose_name="Country")
    created_date = models.DateTimeField(auto_now_add=True, null=False)
    created_by = models.CharField(max_length=255, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=False)
    modified_by = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    captcha_score = models.FloatField(default=0.0)


def __str__(self):
    return f'{self.user}'
