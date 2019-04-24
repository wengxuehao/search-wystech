from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    用户模型
    """
    id = models.IntegerField(primary_key=True,verbose_name='用户编号')
    telephone = models.CharField(max_length=11, verbose_name='手机号',default='')
    password = models.CharField(max_length=10,verbose_name='密码',default='')
    icon = models.ImageField(upload_to='img',default='')

    class Meta:
        verbose_name = '用户模型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.telephone
