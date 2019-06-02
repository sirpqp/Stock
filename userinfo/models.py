from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

sex_choices= (
    (0,'男'),
    (1,'女')
)

class UserInfo(AbstractUser):
    email = models.EmailField(verbose_name='邮箱')
    birth = models.CharField(verbose_name='生日',max_length=20,null=True)
    phone = models.CharField(verbose_name='电话',max_length=20,null=True)
    sex = models.IntegerField(verbose_name='性别',choices=sex_choices,default=0)
    is_active = models.BooleanField(verbose_name='是否激活',default=True)
    is_ban = models.BooleanField(verbose_name='是否禁用',default=False)

    def __str__(self):
        return self.username

    def get_sex(self):
        if self.sex == 0:
            return u'男'
        else:
            return u'女'

class BankCard(models.Model):
    user = models.CharField(verbose_name='持卡人')
    name = models.CharField(verbose_name='持卡人姓名')
    start_time = models.DateTimeField(verbose_name='开卡时间')