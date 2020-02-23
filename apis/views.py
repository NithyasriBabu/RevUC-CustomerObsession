from django.shortcuts import render

# Create your views here.
from apis.models import Products, Households, Transactions
from apis.serializers import ProductsSerializer, HouseholdsSerializer, TransactionsSerializer
from rest_framework import generics

class ProductsListCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class HouseholdsListCreate(generics.ListCreateAPIView):
    queryset = Households.objects.all()
    serializer_class = HouseholdsSerializer

class TransactionsListCreate(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

 