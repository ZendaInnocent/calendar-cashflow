from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:year>/<int:month>/',
         views.month_detail_view, name='month-detail'),
    path('transactions/', views.transactions_view, name='transactions'),
    path('<int:year>/<int:month>/transactions/',
         views.month_transactions_view, name='month-transactions'),
    path('add-transaction/', views.TransactionAddView.as_view(),
         name='add-transaction'),
    path('update-transaction/<pk>/', views.TransactionUpdateView.as_view(),
         name='update-transaction'),
    path('add-account/', views.AccountAddView.as_view(),
         name='add-account'),
    path('update-account/<pk>/', views.AccountUpdateView.as_view(),
         name='update-account'),
    path('accounts-list/', views.AccountsListView.as_view(),
         name='accounts-list'),
]
