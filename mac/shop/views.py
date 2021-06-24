from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
from django.http import HttpResponse
def index(request):
    products=Product.objects.all()
    n=len(products)
    n_slides=ceil(n/4)
    #params={"nslides":range(1,n_slides),'products':products}
    allProds=[[range(1,n_slides), products],[range(1,n_slides), products]]
    params={'allProds':allProds}
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

