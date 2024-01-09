from django.http import Http404
from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView
from .models import Product

class ProductListView(ListView):
    queryset=Product.objects.all()
    template_name="products/product_list.html"

    # def get_context_data(self , *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


def product_list_view(request):
    queryset=Product.objects.all()
    context={"qs":queryset}

    return render(request,'products/product_list.html',context)

class ProductDetailView(DetailView):
    queryset=Product.objects.all()
    template_name="products/product_detail.html"

    def get_context_data(self , *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        context['abc']=123
        print(context)
        return context
    
    def get_object(self,*args, **kwargs):
        request=self.request
        pk=self.kwargs.get('pk')
        instance=Product.objects.get_by_id(pk)

        if instance is None:
            raise Http404('Product does not exist')
        return instance


def product_detail_view(request ,pk=None,*args,**kwargs):
    #instance=Product.objects.get(pk=pk)
    # instance=get_object_or_404(Product , pk=pk)

    # try:
    #     instance=Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here...')
    #     raise Http404('Product does not exist')
    # except:
    #     print("huh ???")
    
    instance=Product.objects.get_by_id(pk)
    #print(instance)

    if instance is None:
        raise Http404('Product does not exist')

    qs=Product.objects.filter(id=pk)
    
    if qs.exists() and qs.count()==1:
        instance=qs.first()
    else:
        raise Http404('Product does not exist')
    context={"object":instance}

    return render(request,'products/product_detail.html',context)

