from django.urls import path
from apis import views

urlpatterns = [
    path('products/', views.ProductsListCreate.as_view()),
    path('households/', views.HouseholdsListCreate.as_view()),
    path('transactions/', views.TransactionsListCreate.as_view()),
]