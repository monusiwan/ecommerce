from django.shortcuts import render,redirect, HttpResponseRedirect
from django.http.response import HttpResponse
from .models.product import *
from .models.category import *
from .models.customer import *
from .models.orders import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.views import *
from ecommerce.middlewares.auth import auth_middleware

# @login_required(login_url='login')
def checkview(request):
    return render(request, 'check.html')
# Create your views here.
class home(View):
    def post(self,request):
        product=request.POST.get('product')
        remove= request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print(cart)
        return redirect('home')

    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        # messages.success(request, "This is Our Home Page")
        products=None
        categories=Category.get_all_categories()
        categoryID=request.GET.get('category')
        if categoryID:
            products=Product.get_all_products_by_categoryid(categoryID)
        else:
            products=Product.get_all_products()
        d={}
        d={'product':products,'categories':categories}
        return render(request, 'home.html',context=d)



   

# ----------signup-----------

def signupView(request):
    # messages.success(request, "Welcome to Our Signup Page")
    if request.method=='GET':
        d={}
        userr=UserCreationForm()
        cus=CustomerForm()
        d={'userr':userr,'cus':cus}
        return render(request, 'signup.html',context=d)
    elif(request.method=="POST"):
        userr=UserCreationForm(request.POST)
        cus=CustomerForm(request.POST)
        if (userr.is_valid() and cus.is_valid()):
            u=userr.save()
            c=cus.save(commit=False)
            c.user=u
            c.save()
            messages.success(request, "Account Created Successfully....")
            return redirect('login')
        else:
            messages.error(request, "username already taken")
            return redirect('signup')
    else:
        userr=UserCreationForm()
        d={'userr':userr}
        return render(request, 'signup.html',context=d)

# ---------------Login--------------

def login_view(request):
    if not request.user.is_authenticated:
        if request.method=='GET':
            fm=AuthenticationForm()
            d={}
            d={'fm':fm}
            return render(request, 'login.html',context=d)
        elif(request.method=='POST'):
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.info(request,f'Login Successfull as {uname}')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password')
                    return redirect('login')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully...')
    return redirect('home')
   

#---------Ipload Products--------
def product_view(request):
    if request.user.is_authenticated:
        d={}
        if request.method=="GET":
            prod=ProductForm()
            d={'prod':prod}
            return render(request, "product.html",context=d)
        elif(request.method=="POST"):
            pass

            
# ---------------Store-----------------
def store_view(request):
    # categories=Category.get_all_categories()
    return render(request, "store.html")

#-------------------Cart-----------------
class Cart(View):
    def get(self,request):
        d={}
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        # print(products)
        d={'products':products}
        return render(request, "cart.html",context=d)


#---------------Check Out-----------------
class Checkout(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.user
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        products  = Product.objects.filter(id__in =ids)
        print(address,phone,customer,cart)       
        for product in products:
            order = Order(customer=customer,product=product,price=product.price,address=address,phone=phone,
            quantity= cart.get(str(product.id)))
            print(order)
            order.save()
        request.session['cart']={}
        return redirect('cart')


# --------------------Orders------------------
# @auth_middleware
def order_view(request):
    d={}
    if request.method=="GET":
        customer = request.user
        orders = Order.get_orders_by_customer(customer)
        # print(orders)
        d={'orders':orders}
    return render(request, 'orders.html',context=d)

