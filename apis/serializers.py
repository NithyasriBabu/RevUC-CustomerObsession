from rest_framework import serializers
from apis.models import Products, Households, Transactions

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_id', 'department', 'commodity', 'brand_type','organic')

class HouseholdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Households
        fields = ('hshd_id', 'loyalty','age_range', 'marital_status','income_range','homeowner','hshd_comp','hh_size','children')

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('hshd_id', 'bskt_id', 'trans_date', 'product_id', 'spend','units','store_region', 'week_num', 'year')