from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth import login, authenticate , logout
from .models import User
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if email and password1:
                try:
                    user = User.objects.create_user(email=email, phone=phone, name=name, password=password1)
                    user.save()
                    user = authenticate(email=email, password=password1)
                    if user is not None:
                        login(request, user)
                        return redirect('product_list')
                except Exception as e:
                    # Handle any errors that may occur
                    print(e)
                    return render(request, 'register.html', {'error': 'A user with this email or phone number already exists.'})
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required(login_url="/login")
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form,'mode':"add"})

@login_required(login_url="/login")
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form': form,"mode":"edit"})

@login_required(login_url="/login")
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'confirm_delete.html', {'product': product})