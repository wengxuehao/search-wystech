from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    用户模型
    """
    telephone = models.CharField(max_length=11, verbose_name='手机号',default='')

    class Meta:
        verbose_name = '用户模型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.telephone
