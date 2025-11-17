from django.shortcuts import render
from .models import Product

def index_view(request):

    new_arrivals = Product.objects.filter(category='New Arrivals').order_by('-id')
    best_sellers = Product.objects.filter(category='Best Sellers')

    context = {
        'new_arrivals': new_arrivals,
        'best_sellers': best_sellers,
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserRegistrationForm, AdminRegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@staff_member_required
def admin_register_view(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = AdminRegistrationForm()
    return render(request, 'registration/admin_register.html', {'form': form})