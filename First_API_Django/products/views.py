from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.http import JsonResponse

from .models import Product,Manufacturer

def product_list(request):
    product = Product.objects.all()
    data={
        "products": list(product.values("pk","name")),
        "products": list(product.values())
    }
    response=JsonResponse(data)
    return response

def product_details(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        data={
            "product":
            {
               "name": product.name,
               "manufacturer":product.manufacturer.name,
               "price": product.price,
               "description":product.description,
               "photo": product.photo.url,
               "price": product.price,
               "shipping_cost":product.shipping_cost,
               "quantity": product.quantity
            }
            }
        response=JsonResponse(data)
    except Product.DoesNotExist:
        response=JsonResponse({"error":{
                                "code ":404,
                                "message": "Product not found"
                            }},status=404)
    return response


def manufacturer_list(request):
    manufacturer=Manufacturer.objects.filter(active=True)
    data={"manufacturers":list(manufacturer.values())}
    response=JsonResponse(data)
    return response


def manufacturer_details(request,pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_product=manufacturer.products.all()
        data={
            "manufacturer":
            {
               "name": manufacturer.name,
               "location":manufacturer.location,
               "active":manufacturer.active,
               "products":list(manufacturer_product.values())
            }
            }
        response=JsonResponse(data)
    except Product.DoesNotExist:
        response=JsonResponse({"error":{
                                "code ":404,
                                "message": "manufacturer not found"
                            }},status=404)
    return response

class ProductListView(ListView):
    model=Product
    template_name="products/product_list.html"

class ProductDetailView(DetailView):
    model=Product
    template_name="products/product_details.html"


