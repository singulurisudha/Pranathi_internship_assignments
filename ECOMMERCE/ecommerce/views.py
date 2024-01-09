from django.http import HttpResponse
from django.shortcuts import render , redirect
from .forms import ContactForm , LoginForm , RegisterForm
from django.contrib.auth import authenticate , login , get_user_model
from django.contrib.auth.models import User

def home_page(request):
    context={
        "title":"Home Page",
        "content":"WELCOME TO THE HOME PAGE",
        
    }
    if request.user.is_authenticated:
        context["premium_content"]="YEAHHHHHHH"
    return render(request, 'home.html',context)
def about_page(request):
    context={
        "title":"About Page",
        "content":"WELCOME TO THE ABOUT PAGE"
    }
    return render(request, 'home.html',context)
def contact_page(request):
    form=ContactForm(request.POST or None)
    context={
        "title":"Contact Page",
        "content":"WELCOME TO THE CONTACT PAGE",
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
   
    
    # if request.method == 'POST':
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('address'))
    return render(request, 'contact/view.html',context)

def login_page(request):
    form=LoginForm(request.POST or None)

    context={
        "form":form
    }
    print("User Logged In")
    print(request.user.is_authenticated)

    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user= authenticate(request,username=username,password=password)
        print(request.user.is_authenticated)
        context['form']=LoginForm()

        if user is not None:
           # print(request.user.is_authenticated)
            login(request,user)
            return redirect("/login")
        else:
            print("Error")

    return render(request,'auth/login.html',context)

User=get_user_model()
def register_page(request):
     form=RegisterForm(request.POST or None)
     context={
         "form":form
     }
     if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        new_user=User.objects.create_user(username,email,password)
        print(new_user)
     return render(request,'auth/register.html',context)