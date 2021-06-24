from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
from django.http import HttpResponse
def index(request):
    prods=Product.objects.all()
    n=len(prods)
    n_slices=ceil(n/4)
    params={"nslices":range(1,n_slices),'products':prods}
    return render(request,'shop/index.html',params)
def about(request):
    return HttpResponse('We are on the about page')
def contact(request):
    return HttpResponse('We are on the Contact us page')
def tracker(request):
    return HttpResponse('We are on the Tracker page')
def search(request):
    return HttpResponse('We are on the Search page')
def productView(request):
    return HttpResponse('We are on the Product View page')
def checkout(request):
    return HttpResponse('We are on the Checkout page')

