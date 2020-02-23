from django.urls import path
from apis import views

urlpatterns = [
    path('products/', views.all_products,name='all_products'),
    path('products/<int:id>', views.product_by_ID,name='product_by_ID'),
    path('households/', views.all_households,name='all_households'),
    path('transactions/', views.all_transactions,name='all_transactions'),
    path('transactions/<int:hshd_id>/<int:id>', views.transaction_by_ID,name='transaction_by_ID'),
]