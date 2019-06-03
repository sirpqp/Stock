from django.db import models
from django.contrib.auth.models import AbstractUser
from stocks.models import *

SEX_CHOICES= (
    (0,'男'),
    (1,'女')
)

BANKCARD_CHOICES = (
    (0,'冻结'),
    (1,'正常'),
    (2,'挂失'),
    (3,'注销'),
)

BANK_CHOICES = (
    (0,'ICBC'),
    (1,'CBC'),
    (2,'CCB'),
    (3,'BC'),
    (4,'ABC'),
    (5,'CDB'),
    (6,'CMSB'),
)

# 用户表
class UserInfo(AbstractUser):
    email = models.EmailField(verbose_name='邮箱')
    birth = models.CharField(verbose_name='生日',max_length=20,null=True)
    phone = models.CharField(verbose_name='电话',max_length=20,null=True)
    sex = models.IntegerField(verbose_name='性别',choices=SEX_CHOICES,default=0)
    is_active = models.BooleanField(verbose_name='是否激活',default=True)
    is_ban = models.BooleanField(verbose_name='是否禁用',default=False)

    def __str__(self):
        return self.username

    def get_sex(self):
        if self.sex == 0:
            return u'男'
        else:
            return u'女'

# 银行卡表
class BankCard(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='持卡人')
    name = models.CharField(verbose_name='持卡人姓名',max_length=20,null=True)
    start_time = models.DateTimeField(verbose_name='开卡时间')
    status = models.IntegerField(verbose_name='卡状态',choices=BANKCARD_CHOICES,default=1)
    cardNO = models.CharField(verbose_name='卡号',max_length=50,null=True)
    bank = models.IntegerField(verbose_name='开户行',choices=BANK_CHOICES,default=0)
    trapwd = models.CharField(verbose_name='交易密码',max_length=200,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '银行卡表'
        verbose_name_plural = verbose_name

# 钱包表
class Wallet(models.Model):
    user = models.OneToOneField(UserInfo,verbose_name='用户')
    money = models.DecimalField(verbose_name='资金',max_digits=8,decimal_places=2)
    frozen_money = models.DecimalField(verbose_name='冻结资金',max_digits=8,decimal_places=2)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '钱包表'
        verbose_name_plural = verbose_name

# 持仓表
class Hold(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    stock = models.ForeignKey(Stock,verbose_name='股票')
    amount = models.IntegerField(verbose_name='持仓数量')
    frozen = models.IntegerField(verbose_name='冻结股票')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '持仓表'
        verbose_name_plural = verbose_name



