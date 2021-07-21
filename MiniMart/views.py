from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.forms.models import inlineformset_factory
from django.http import request
from django.http.response import HttpResponse
from MiniMart.forms import FilterForm, Register_Form, OrderForm, user_update
from MiniMart.models import Customer, Order
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user, unauthenticated

# Create your views here.

def home(request):  
    return render(request, "Minimart/home.html")

@allowed_user(allowed_roles=['Admin', 'staff'])
@login_required(login_url = 'login')
def dashboard(request):
    customers  = Customer.objects.all()
    total_orders = Order.objects.all().count()
    pending = Order.objects.filter(status = "Pending").count()
    delivered = Order.objects.filter(status = "Delivered").count()
    details = Order.objects.all()

    FilterFormSet = FilterForm()
    FilterFormSet = FilterForm( request.GET , queryset= details)
    details = FilterFormSet.qs

    context = { 'FilterFormSet': FilterFormSet, 'customers' : customers ,'total_orders' : total_orders, 'pending': pending, 'delivered' : delivered, 'details' : details}
    return render(request, "Minimart/dashboard.html", context)


def carts(request):  
    return render(request, "Minimart/carts.html")


def checkout(request):  
    return render(request, "Minimart/checkout.html")


@allowed_user(allowed_roles=['customer', 'Admin', 'staff'])
@login_required(login_url = 'login')
def about(request, id_num):
    customer = Customer.objects.get(id = id_num)
    total_orders = customer.order_set.all().count()
    order = customer.order_set.all()
    delivered = order.filter(status = "Delivered").count()
    pending = order.filter(status = "Pending").count()


    context = {'total_orders' : total_orders, 'customer' : customer, 'order': order, 'pending': pending, 'delivered' : delivered}
    return render(request, "Minimart/About.html", context)



def register(request):
    Registerform = Register_Form()
    if request.method == 'POST':
        Registerform = Register_Form(request.POST)
        if Registerform.is_valid():
            profile = Registerform.save()
            group = Group.objects.get(name = "customer")
            profile.groups.add(group)

            messages.success(request, "Your account was created")
            return redirect('login')
    context = { 'Registerform' : Registerform,}
    return render(request, "Minimart/register.html", context)


def profile(request):
    # customer = request.user.customer

    context = {}
    return render(request, "Minimart/profile.html", context)


def edit_profile(request):
    update_form = user_update(instance = request.user.customer)
    if request.method == 'POST':
        update_form = user_update(request.POST, request.FILES ,instance=request.user.customer)
        if update_form.is_valid:
            update_form.save()
            print(update_form)
            return redirect('about', request.user.customer.id)

    context = {'update_form': update_form}
    return render(request, "Minimart/edit_profile.html", context)



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            if (user.customer.name or user.customer.phone or user.customer.email ) == None:
                return redirect('edit_profile')
            else:
                return redirect('home')
        else:
            messages.info(request, 'username or password was incorect')

    context = {}
    return render(request, "Minimart/login.html", context)


def denied(request):
    return HttpResponse("***you are not authorized to this Action.. Contact Admin***")


@login_required(login_url = 'login')
def logout(request):
    auth_logout(request)
    return redirect('login')



@login_required(login_url = 'login')
def create_order(request, pk):
    customer = Customer.objects.get( id = pk)
    orderSet = inlineformset_factory( Customer, Order, fields= ('Product', 'status'), extra= 5)
    formset = orderSet(queryset = Order.objects.none() , instance = customer)
    if request.method == 'POST':
        formset = orderSet(request.POST ,instance = customer)
        if formset.is_valid():
            formset.save()

            return redirect('about', pk)

    context = {'OrderSetForm' : orderSet , "customer" : customer}
    return render(request, 'MiniMart/create_order.html', context)


@login_required(login_url = 'login')
def delete_order(request, pk):
    order = Order.objects.get(id = pk)
    delete_form = OrderForm(instance= order)
    if request.method == 'POST':
        order.delete()
        return redirect('about', order.Customer.id )

    context = { 'order' : order, 'delete_form' : delete_form}
    
    return render(request, 'MiniMart/delete_order.html', context)


@login_required(login_url = 'login')
def update_order(request, pk):
    order = Order.objects.get( id = pk)
    customer = order.Customer.id
    form = OrderForm( instance=order )
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('about', order.Customer.id)

    context = { 'form' : form, 'order': order}
    
    return render(request, 'MiniMart/update_order.html', context)