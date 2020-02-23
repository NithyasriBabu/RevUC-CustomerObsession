from django.db import models

class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=10)
    commodity = models.CharField(max_length=25)
    brand_type = models.CharField(max_length=10)
    organic = models.BooleanField()


class Households(models.Model):
    hshd_id = models.IntegerField(primary_key=True)
    loyalty = models.BooleanField()
    age_range = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=10)
    income_range = models.CharField(max_length=15)
    homeowner = models.CharField(max_length=10)
    hshd_comp = models.CharField(max_length=20)
    hh_size = models.CharField(max_length=3)
    children = models.CharField(max_length=3)

class Transactions(models.Model):
    hshd_id = models.IntegerField()
    bskt_id = models.IntegerField()
    trans_date = models.DateField(auto_now=True)
    product_id = models.IntegerField()
    spend = models.FloatField()
    units = models.IntegerField()
    store_region = models.CharField(max_length=10)
    week_num = models.IntegerField()
    year = models.IntegerField()