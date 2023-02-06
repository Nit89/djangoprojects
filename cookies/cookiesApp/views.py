from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm

# Create your views here.
def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h2>Home page</h2>")


def page2(request):
    if request.session.test_cookie_worked():
        print('cookies are enabled')
        request.session.delete_test_cookie() 
    return HttpResponse("<b>page2</b>")


def countView(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count'])+1
    else:
        count = 1
    response=render(request,'count.html',{'count':count})
    response.set_cookie('count',count)
    return response

def index(request):
    return render(request,'index.html')



def addItem(request):
    form = ItemForm()
    response = render(request,'addItem.html',{'form':form})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity,120)
    return response

            
        
        
def displayCart(request):
    return render(request,'displayItem.html')

