from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.forms import inlineformset_factory
from .forms import OrderForm,CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def Loginpage(request):
   if request.method == 'POST':
     username=  request.POST.get('username')
     password = request.POST.get('password')
     user = authenticate(request,username=username, password=password)
     if user is not None:
      login(request,user)
      return redirect('home')
     else:
        messages.info(request,'username and password incorrect ! ')
        return render(request,'accounts/login.html')
   context ={}
   return render(request,'accounts/login.html',context)

def logoutuser(request):
   logout(request)
   return redirect('login')


def logoutuser(request):
   logout(request)
   return redirect('login')


def Registerpage(request):
   form = CreateUserForm()
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         messages.success(request,'Account created for '+ user)
         return redirect('login')
   context = {'form':form} 
   return render(request,'accounts/register.html',context)

def home(request):
   orders = Order.objects.all()
   customers = Customer.objects.all()

   total_orders = orders.count()
   orders_deliverd = orders.filter(status='Delivered').count()
   orders_pending = orders.filter(status='Pending').count()

   context = {'orders':orders,'customers':customers,'total_orders':total_orders,'orders_deliverd':orders_deliverd,'orders_pending':orders_pending}
   #return HttpResponse('Home page')
   return render(request,'accounts/dashboard.html',context)


def products(request):
   products = Product.objects.all()
   return render(request,'accounts/products.html',{'products':products})
#   return HttpResponse('product page')

def customers(request,pk_test):
   customer = Customer.objects.get(id=pk_test)
   orders = customer.order_set.all()
   order_count = orders.count()
   myFilter = OrderFilter( request.GET, queryset=orders)
   orders = myFilter.qs
   context = {'customer':customer,'orders':orders,'order_count':order_count,'myFilter':myFilter}
   return render(request,'accounts/customers.html',context)
   # return HttpResponse('customers page')

def createOrder(request,pk):
   OrderFormSet = inlineformset_factory(Customer,Order, fields=('product','status'),extra=4)
   customer = Customer.objects.get(id=pk)
   formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
   #form = OrderForm(initial={'customer': customer})
   if request.method == 'POST':
      # print('Print post data :', request.POST)
      #form = OrderForm(request.POST)
      formset = OrderFormSet(request.POST,instance=customer)
      if formset.is_valid():
         formset.save()
         return redirect('/')

   context = {'formset': formset}
   return render(request,'accounts/order_form.html',context)

def updatOrder(request,pk):
   order = Order.objects.get(id=pk)
   form = OrderForm(instance=order)
   if request.method == 'POST':
      # print('Print post data :', request.POST)
      form = OrderForm(request.POST,instance=order)
      if form.is_valid():
         form.save()
         return redirect('/')
   

   
   context = {'form':form}
   return render(request,'accounts/order_form.html',context)

def deleteOrder(request,pk):
   order = Order.objects.get(id=pk)
   if request.method == 'POST':
      order.delete()
      return redirect('/')
   context ={'item':order}
   return render(request,'accounts/deleteform.html',context)