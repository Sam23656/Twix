from django.http import HttpResponse
from django.shortcuts import render

from factory2.models import Product


# Create your views here.

def show_product_page(request, product_id):
    return render(request, "product.html", context={"product": Product.objects.get(pk=product_id)})


def show(request):
    return HttpResponse("<h1>True</h1>")
