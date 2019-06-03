from django.db import models
from userinfo.models import *
from stocks.models import *


ROLE_CHOICES = (
    (0,'买'),
    (1,'卖'),
)

# 自选股
class SelfStcok(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    stock = models.ForeignKey(Stock,verbose_name='股票')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '交易表'
        verbose_name_plural = verbose_name

# 挂单表
class BOSStock(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    stock = models.ForeignKey(Stock,verbose_name='股票')
    role = models.IntegerField(verbose_name='买卖角色',choices=ROLE_CHOICES,default=0)
    amount = models.IntegerField(verbose_name='数量')
    price = models.DecimalField(verbose_name='价格',max_digits=8,decimal_places=2)
    datetime = models.DateTimeField(verbose_name='挂单时间',auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '挂单表'
        verbose_name_plural = verbose_name

# 交易记录表
class DealList(models.Model):
    orderid = models.CharField(verbose_name='交易记录号',max_length=20,null=False)
    datetime = models.DateTimeField(verbose_name='交易时间', auto_now_add=True)
    price = models.DecimalField(verbose_name='成交价格', max_digits=8, decimal_places=2)
    amount = models.IntegerField(verbose_name='数量')
    stock = models.CharField(verbose_name='股票',max_length=20,null=False)
    buser = models.ForeignKey(UserInfo,verbose_name='买家',related_name='buser')
    suser = models.ForeignKey(UserInfo,verbose_name='卖家',related_name='suser')

    def __str__(self):
        return self.orderid

    class Meta:
        verbose_name = '交易记录表'
        verbose_name_plural = verbose_name