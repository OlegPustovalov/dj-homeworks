from django.shortcuts import render, redirect
from django.http import HttpResponse

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
     str_ = request.GET.get("sort",'name')
     print(str_)
     template = 'catalog.html'
     if str_ == 'min_price':
         phones_obj = Phone.objects.all().order_by('price')
     elif str_ == 'max_price':
         phones_obj = Phone.objects.all().order_by('-price')
     else:
         phones_obj = Phone.objects.all().order_by('name')
     context = {
        'phones': phones_obj
    }
     return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_obj = Phone.objects.filter(slug = slug)
    phone={}
    for c in phones_obj:
        phone={'name':c.name,'price':c.price,'release_date':c.release_date,'image':c.image,'lte_exists':c.lte_exists,'slug':slug}
    context=phone
    return render(request, template, context)
