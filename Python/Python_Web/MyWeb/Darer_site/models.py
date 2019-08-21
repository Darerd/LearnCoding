from django.db import models

# Create your models here.

class Goods(models.Model):
	goods_name = models.CharField(max_length = 30)  # 字符串类型（CharField）
	goods_number = models.IntegerField()			# 整数类型（IntegerField）
	goods_price = models.FloatField()				# 浮点数类型（FloatField）
    #goods_sales = models.IntegerField(default = 0)
