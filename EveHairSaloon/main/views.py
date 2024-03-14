from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import ProductForm,LoginForm
from .models import Product
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successfully')

            return redirect('home',)
    else:
        form = UserCreationForm()

    return render(request, 'main/registration.html',{'form':form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                 return render(request, 'main/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to the homepage or any other desired page after logout
    return redirect('login')




def home(request):
    products = Product.objects.all()
    #dd(products)

    return render(request, 'main/index.html', {'products': products})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Assuming quantity is submitted via POST

    if request.user.is_authenticated:
        user_id = request.user.id
        # Check if the product is already in the user's cart
        cart_item = Cart.objects.filter(user_id=user_id, product_id=product_id).first()
        if cart_item:
            # If the item is already in the cart, update the quantity
            cart_item.quantity += quantity
            cart_item.save()
        else:
            # If the item is not in the cart, create a new cart item
            cart_item = Cart.objects.create(user_id=user_id, product_id=product_id, quantity=quantity)
    else:
        # If the user is not authenticated, handle as desired (e.g., anonymous cart)
        pass

    return redirect('cart')  # Assuming you have a URL named 'cart'


def cart(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        cart_items = Cart.objects.filter(user_id=user_id)
    else:
        # Handle anonymous cart here if needed
        cart_items = []

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    #dd(sum(cart_items))
    return render(request, 'main/cart.html', {'cart_items': cart_items, 'total_price': total_price})
    
    
    



def products_list(request):
    products = Product.objects.all()

    return render(request, 'main/products_list.html', {'products': products})

def add_product(request):
    
    submitted = False
    if request.method == 'POST':
        
        form = ProductForm(request.POST, request.FILES)
        #dd(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('cart')
    else:
        form = ProductForm()
        if submitted in request.GET:
            submitted = True
            
    return render(request, 'main/add_product.html', {'form': form, 'submitted': submitted})
