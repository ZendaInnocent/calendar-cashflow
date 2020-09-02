from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/',
         views.month_detail_view, name='month-detail'),
    path('transactions/', views.transactions_view, name='transactions'),
    path('<int:year>/<int:month>/transactions/',
         views.month_transactions_view, name='month-transactions'),
]
