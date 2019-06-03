from django.db import models

# Create your models here.
# 广告表
class AdLink(models.Model):
    ad_url = models.URLField(verbose_name='广告链接',null=True)
    title = models.CharField(verbose_name='广告名称',max_length=50,null=True)
    ad_img = models.ImageField(verbose_name='广告图片',upload_to='img/banner',default='normal.png')
    is_show = models.BooleanField(verbose_name='是否显示',default=False)

    def __str__(self):
        return self.title

    class Meta:
        # db_table = "AdLink"
        verbose_name = "广告表"
        verbose_name_plural = verbose_name
        # ordering = ['-id']



# 股票数据
class Stock(models.Model):
    stonumber = models.CharField(verbose_name='股票代码',max_length=20,null=False,default='000000')
    company_name = models.CharField(verbose_name='公司名称',max_length=50,null=True)
    industry = models.CharField(verbose_name='细分行业',max_length=50,null=True)
    area = models.CharField(verbose_name='地区',max_length=50,null=True)
    pe = models.DecimalField(verbose_name='市盈率',max_digits=8,decimal_places=2,null=True)
    outstanding = models.DecimalField(verbose_name='流通股本',max_digits=8,decimal_places=2,null=True)
    totals = models.DecimalField(verbose_name='总股本',max_digits=8,decimal_places=2,null=True)
    totalAssets = models.DecimalField(verbose_name='总资产',max_digits=8,decimal_places=2,null=True)
    liquidAssets = models.DecimalField(verbose_name='流动资产',max_digits=8,decimal_places=2,null=True)
    fixAssets = models.DecimalField(verbose_name='固定资产',max_digits=8,decimal_places=2,null=True)
    reserved = models.DecimalField(verbose_name='公积金',max_digits=8,decimal_places=2,null=True)
    reservedPerShare = models.DecimalField(verbose_name='每股公积金',max_digits=8,decimal_places=2,null=True)
    esp = models.DecimalField(verbose_name='每股收益',max_digits=8,decimal_places=2,null=True)
    bvps = models.DecimalField(verbose_name='每股净资产',max_digits=8,decimal_places=2,null=True)
    pb = models.DecimalField(verbose_name='市净率',max_digits=8,decimal_places=2,null=True)
    timeToMarcket = models.DateField(verbose_name='上市日期')

    def __str__(self):
        return self.stonumber

    class Meta:
        verbose_name="股票表"
        verbose_name_plural=verbose_name

# 股票咨询表
class StockNews(models.Model):
    title = models.CharField(verbose_name='标题',max_length=50,null=True)
    detail = models.TextField(verbose_name='详细内容')
    time = models.DateTimeField(verbose_name='发布时间',auto_now_add=True)
    author = models.CharField(verbose_name='作者',max_length=20,null=True)
    is_delete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="股票咨询表"
        verbose_name_plural = verbose_name