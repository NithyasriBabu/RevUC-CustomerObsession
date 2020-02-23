from django.urls import path
from apis import views

urlpatterns = [
    path('products/', views.all_products,name='all_products'),
    path('households/', views.all_households,name='all_households'),
    path('transactions/', views.all_transactions,name='all_transactions'),
]