from django.http import HttpResponse
from django.urls import path, re_path
from factory2.views import show_product_page, show

app_name = 'factory2'

urlpatterns = [
    re_path(r'^(?P<product_id>\d+)/$', show_product_page, name="product_page")
]
