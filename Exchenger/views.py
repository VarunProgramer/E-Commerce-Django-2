from django.shortcuts import render, redirect
from .forms import *
from .models import codegery, prodect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def home (request):
    codegerys = codegery.objects.all()
    prodects = prodect.objects.all()
    context = {
        'cadagorys' : codegerys, 
        'products' : prodects
}
    return render(request, 'Exchenger/intex.html', context)


def register (request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    return render(request, 'registration/sign_up.html', {'form' : form})

@login_required(login_url='/login')
def product_list_form(request):
    if request.method == 'POST':
        form = ProdectForm(request.POST, request.FILES, Prodect_oner_id =User)        
        print('varun kumar 1')
        if form.is_valid():
            form.save()
            print('varun kumar 2')
            return redirect('/home')
    else:
        form = ProdectForm()
    return render(request, 'Exchenger/prodect_list_form.html', {'form' : form})

def product_list(request, id):
    if(codegery.objects.filter(id = id)):
        products = prodect.objects.filter(codegery_type_id = id)
        return render(request, 'Exchenger/product_list.html', {'products' : products})
    else:
        messages.warning(request, "Codegery not found")
        return redirect('/home')
    
def product_details(request, id):
    product = prodect.objects.get(id = id)
    return render(request ,'Exchenger/product_details.html', {'product' : product})

def codegery_creation(request):
    if request.method == 'POST':
        form = CodegeryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = CodegeryForm()
    return render(request, 'Exchenger/Codegery_creation_Form.html', {'form' : form})

def search_box(request):
    q = request.GET.get('q')
    multiple_Q = Q(Q(codegery_type__name__icontains = q) | Q(Prodect_oner__username__icontains = q) | Q(name__icontains = q))
    result = prodect.objects.filter(multiple_Q)
    if result:
        results = result
    elif (q == 'all') or (q == 'All'):
        results = prodect.objects.all()
    else:
        results = None
    context = {
        'products' : results
    }
    return render (request,'Exchenger/product_list.html', context)

def notification(request):
    return render(request, 'Exchenger/notification.html')

def message(request):
    return render(request, 'Exchenger/message.html')

def chat_box(request):
    return render(request, 'Exchenger/chatbox.html')