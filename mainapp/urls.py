from django.urls import path

from mainapp.views import index, about, contacts, product, products

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('product/', product, name='product'),
    path('products/', products, name='products'),
]
