from django.shortcuts import render, redirect
from .models import Cart, Customer, Product, OrderPlaced
from django.views import View
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):

    def get(self, request):
        topwears = Product.objects.filter(category="TW")
        bottomwears = Product.objects.filter(category="BW")
        mobiles = Product.objects.filter(category="M")
        laptops = Product.objects.filter(category="L")
        return render(request, 'app/home.html', { 'topwears':topwears ,'bottomwears':bottomwears ,'mobiles': mobiles, 'laptops':laptops })


class ProductDetailView(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':product})



def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product_obj = Product.objects.get(id=product_id)
    user = request.user
    if Cart.objects.filter(product = product_obj, user= request.user):
        return redirect('/cart')
    Cart(user=user, product=product_obj).save()
    return redirect('/cart')


def showcart(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)

        amount = 0.0
        shipping_amount = 70
        totalamount = 0.0

        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                temp_ammount = p.quantity * p.product.selling_price
                amount += temp_ammount            
            totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':carts, 'totalamount':totalamount, 'amount' : amount })
        else:
            return render(request, 'app/emptycart.html',)


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70
        totalamount = 0.0
        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_ammount = p.quantity * p.product.selling_price
            amount += temp_ammount            
        totalamount = amount + shipping_amount
        data = {
            'quantity':c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70
        totalamount = 0.0
        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_ammount = p.quantity * p.product.selling_price
            amount += temp_ammount            
        totalamount = amount + shipping_amount

        data = {
            'quantity':c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)




def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70
        totalamount = 0.0
        cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_ammount = p.quantity * p.product.selling_price
            amount += temp_ammount            
        totalamount = amount + shipping_amount

        data = {
            'quantity':c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):    
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            lacality = form.cleaned_data['lacality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']

            res = Customer(user = user, name=name, lacality=lacality, city=city, zipcode=zipcode, state=state )
            res.save()
            messages.success(request, 'the data is updated successfully !!')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
        

def address(request):
    address_list = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'address_list': address_list, 'active':'btn-primary'})

def orders(request):
    print(request.user)
    placedorder = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'orders':placedorder})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category = "M")
    elif data=="redmi" or data=="samsung" or data=="realmi" or data=="apple" or data=="oneplus":
        mobiles = Product.objects.filter(category = "M").filter(brand=data)
    elif data=='below':
        mobiles= Product.objects.filter(category="M", selling_price__lt=20000)
    elif data=='above':
        mobiles= Product.objects.filter(category="M", selling_price__gt=20000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})
        

def login(request):
 return render(request, 'app/login.html')

class  CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations !! Registered Successfully')
        return render(request, 'app/customerregistration.html', {'form':form})

def checkout(request):
    user = request.user
    address = Customer.objects.filter(user =user)
    cart_items = Cart.objects.filter(user=request.user)
    amount = 0.0
    shipping_amount = 70
    totalamount = 0.0
    cart_product = [ p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            temp_ammount = p.quantity * p.product.selling_price
            amount += temp_ammount            
        totalamount = amount + shipping_amount
            
    all_data = {'address' :address,'amount':amount, 'totalamount':totalamount, 'cart_items':cart_items }
    return render(request, 'app/checkout.html', context=all_data)



def payment_done(request):
    print(11111111111111111111111111)
    present_user = request.user
    custid = request.GET.get('custid')
    print(22222222222, custid)
    customer = Customer.objects.get(id=custid)
    user_cart_items = Cart.objects.filter(user=present_user)

    for item in user_cart_items:
        OrderPlaced(user=present_user, customer=customer, product = item.product, quantity= item.quantity).save()
        item.delete()
    return redirect('orders')