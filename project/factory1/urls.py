from django.urls import path
from factory1.views import show_product_page

urlpatterns = [
    path('<int:product_id>/', show_product_page, name="product_info")
]
