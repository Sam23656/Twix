from django.shortcuts import render

from factory1.models import Product
from factory2.models import Product as Product2


# Create your views here.

def show_index_page(request):
    return render(request, "index.html",
                  context={"factory1": Product.objects.all(), "factory2": Product2.objects.all()})


def show_product_page(request, product_id):
    return render(request, "product.html", context={"product": Product.objects.get(pk=product_id)})

