from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
from django.http import HttpResponse
def index(request):
    #products=Product.objects.all()
    #n=len(products)
    #n_slides=ceil(n/4)
    #params={"nslides":range(1,n_slides),'products':products}
    #allProds=[[range(1,n_slides), products],[range(1,n_slides), products]]
    allProds=[]
    wholelist=Product.objects.values('category')
    categories={item['category'] for item in wholelist}
    for cat in categories:
        catproducts=Product.objects.filter(category=cat)
        n=len(catproducts)
        n_slides=ceil(n/4)
        allProds.append([range(1,n_slides),catproducts])

    params={'allProds':allProds}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,'shop/search.html')
def products(request,myid):
    # We need to fetch the product using the ID
    prod=Product.objects.filter(id=myid)
    return render(request,'shop/products.html',{'product':prod[0]})
    #We used prod[0] as prod is a list of single item, ans list cant be used there.
def checkout(request):
    return render(request,'shop/checkout.html')

