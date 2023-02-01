from django.shortcuts import render

# Create your views here.

def electronics(request):
    product_dist= {
        'product1': 'Mac',
        'product2': 'samsung',
        'product3': 'android',
    }
    return render(request,'product.html',product_dist)
    
def toys(request):
   product_dist= {
        'product1': 'drone',
        'product2': 'ps3',
        'product3': 'remotecar',
   }
   return render(request,'product.html',product_dist)

def shoes(request):
   product_dist= {
        'product1': 'Nike',
        'product2': 'Addidas',
        'product3': 'Reebok',
   }
   return render(request,'product.html',product_dist)

def index(request):
   return render(request,'index.html')
