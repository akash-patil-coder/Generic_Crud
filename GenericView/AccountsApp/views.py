from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def loginView(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        print(un)
        print(pw)
        user = authenticate(username=un,password=pw)
        if user is not None:
            login(request,user)
            #subject = 'welcome to Django world'
            #message = f'Hi {user.username}, thank you for registering in CBVproject.'
            #email_from = settings.EMAIL_HOST_USER
            #recipient_list = ['akashpatil9009@gmail.com' ]
            #send_mail(subject, message, email_from, recipient_list)
            return redirect('list_laptop')
        else:
            messages.error(request,'Invalid Credentials !')
    context = {}
    template_name = 'AccountsApp/login.html'
    return render(request, template_name, context)

def registrationView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    template_name = 'AccountsApp/register.html'
    return render(request, template_name, context)



def logoutView(request):
    logout(request)
    return redirect('login')
