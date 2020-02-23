from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from apis.models import Products, Households, Transactions

def all_products(request):
    products = Products.objects.all()
    results = {
        'count': len(products),
        'results': list(products.values('product_id', 'department', 'commodity', 'brand_type','organic'))
    }
    return JsonResponse(results)

def product_by_ID(request, id):
    product = Products.objects.get(product_id=id)
    results = {'product_id': product.product_id, 
                'department': product.department, 
                'commodity': product.commodity, 
                'brand_type': product.brand_type,
                'organic': product.organic}
    return JsonResponse(results)

def all_households(request):
    households = Households.objects.all()
    results = {
        'count': len(households),
        'results': list(households.values('hshd_id', 'loyalty','age_range', 'marital_status','income_range','homeowner','hshd_comp','hh_size','children'))
    }
    return JsonResponse(results)

def households_by_ID(request, id):
    household = Households.objects.get(hshd_id=id)
    results = { 'hshd_id': household.hshd_id, 
                'loyalty': household.loyalty,
                'age_range': household.age_range, 
                'marital_status': household.marital_status,
                'income_range': household.income_range,
                'homeowner': household.homeowner,
                'hshd_comp': household.hshd_comp,
                'hh_size': household.hh_size,
                'children': household.children}
    return JsonResponse(results)

def all_transactions(request):
    transactions = Transactions.objects.all()
    results = {
        'count':len(transactions),
        'results': list(transactions.values('hshd_id', 'bskt_id', 'trans_date', 'product_id', 'spend','units','store_region', 'week_num', 'year'))
    }
    return JsonResponse(results)

def transaction_by_ID(request, hshd_id, id):
    transactions = Transactions.objects.filter(hshd_id=hshd_id,bskt_id=id)
    if transactions:
        household = Households.objects.get(hshd_id=hshd_id)
        transactions_results = []
        for transaction in transactions:
            transactions_results.append({
                'hshd_id': hshd_id, 
                'bskt_id': id, 
                'trans_date': transaction.trans_date, 
                'product_id': transaction.product_id, 
                'product_data': list(Products.objects.filter(product_id=transaction.product_id).values('product_id', 'department', 'commodity', 'brand_type','organic')),
                'spend': transaction.spend,
                'units': transaction.units,
                'store_region': transaction.store_region, 
                'week_num': transaction.week_num, 
                'year': transaction.year
            })
        
        results = {
            'count': len(transactions),
            'results': {
                'household': { 
                    'hshd_id': household.hshd_id, 
                    'loyalty': household.loyalty,
                    'age_range': household.age_range, 
                    'marital_status': household.marital_status,
                    'income_range': household.income_range,
                    'homeowner': household.homeowner,
                    'hshd_comp': household.hshd_comp,
                    'hh_size': household.hh_size,
                    'children': household.children
                },
                'transactions':  transactions_results
            }
        }
        return JsonResponse(results)
    return JsonResponse({})



'''
    ('hshd_id', 'bskt_id', 'trans_date', 'product_id', 'spend','units','store_region', 'week_num', 'year'))}
    results = { 'hshd_id': household.hshd_id, 
                'loyalty': household.loyalty,
                'age_range': household.age_range, 
                'marital_status': household.marital_status,
                'income_range': household.income_range,
                'homeowner': household.homeowner,
                'hshd_comp': hshd_comp,
                'hh_size': household.hh_size,
                'children': household.children}
    return JsonResponse(results)
'''