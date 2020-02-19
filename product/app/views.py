from django.shortcuts import render,redirect
from . models import Product
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def addproductView(request):
    if request.method == 'POST':
        prodId = request.POST['prodId']
        prodPrice = request.POST['prodPrice']
        prodStock = request.POST['prodStock']
        prodName = request.POST['prodName']

        try:
            edited= Product.objects.get(product_id = prodId)
            if edited:
                edited.product_id = prodId
                edited.price = prodPrice
                edited.stock = prodStock
                edited.name = prodName
                edited.save()
        except:
            product=Product.objects.create(product_id=prodId, price=prodPrice, stock=prodStock, name = prodName)
            product.save()
    products = Product.objects.all()
    return render(request,'addproduct.html',{'products':products})

def deleteView(request):
    if request.method == 'POST':
        product = Product.objects.get(product_id=request.POST.get('id'))
        product.delete()
    return redirect('app:addproduct_url')

def editView(request):
    if request.method == 'POST':
        prodcts = Product.objects.get(product_id=request.POST.get('id'))
        return render(request,'addproduct.html',{'prodcts':prodcts})