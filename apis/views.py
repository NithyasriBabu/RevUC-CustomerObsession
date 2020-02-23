from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from apis.models import Products, Households, Transactions

def all_products(request):
    products = Products.objects.all()
    results = {'results': list(products.values('product_id', 'department', 'commodity', 'brand_type','organic'))}
    return JsonResponse(results)

def all_households(request):
    households = Households.objects.all()
    results = {'results': list(households.values('hshd_id', 'loyalty','age_range', 'marital_status','income_range','homeowner','hshd_comp','hh_size','children'))}
    return JsonResponse(results)

def all_transactions(request):
    transactions = Transactions.objects.all()
    results = {'results': list(transactions.values('hshd_id', 'bskt_id', 'trans_date', 'product_id', 'spend','units','store_region', 'week_num', 'year'))}
    return JsonResponse(results)
