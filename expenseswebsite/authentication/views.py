from collections.abc import Callable, Iterable, Mapping
from typing import Any
from django.shortcuts import render,redirect
# Create your views here.
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator

 
from django.utils.encoding import force_bytes,force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site 
from .utils import token_generator
import threading

class EmailThread(threading.Thread):
    
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    
    def run(self):
        self.email.send(fail_silently=False)
        
         

class EmailValidationView(View):
    def post(self, request):
        data= json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'},status=400) 
        if  User.objects.filter(email = email).exists():
            return JsonResponse({'email_error': 'Email already exist'},status=409) 
        return JsonResponse({'email_valid':True})






class UsernameValidationView(View):
    def post(self, request):
        data= json.loads(request.body)
        username = data['username']
        if  not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should contain only alphanumeric characters'},status=400) 
        if  User.objects.filter(username = username).exists():
            return JsonResponse({'username_error': 'Username already exist'},status=409) 
        return JsonResponse({'username_valid':True})
            
    
class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')    
    
    def post(self, request):
        #GET USER DATA
        #VALIDATE
        #CREATE A USER ACCOUNT
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        context = {
            
            'fieldValues':request.POST
        }
        if not User.objects.filter(username= username).exists():
            if not User.objects.filter(email= email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password  too short')
                    return render(request, 'authentication/register.html',context)
                
                user = User.objects.create_user(username=username, email=email,)    
                user.set_password(password)         
                user.is_active = False
                user.save()
                #path to view
                # getting the domain we are on
                #relative url to verification
                #incode  user id (uidb64)
                #token for user to verify
                
                domain = get_current_site(request).domain
                uidb64 =urlsafe_base64_encode(force_bytes(user.pk))
            
                link=reverse('activate',kwargs={'uidb64':uidb64,'token': token_generator.make_token(user)})
              
            
                activate_url='http://'+domain+link 
                email_body= 'Hi '+ user.username+' please use this link to verify your account \n'+activate_url
                email_subject = 'Activate your account'
                email = EmailMessage(
                        email_subject,
                        email_body,
                         'noreply@test.com',
                        [email],
                    )
                EmailThread(email).start()
                        
                messages.success(request, 'Account successfully created,Check out your Email to activate it.')
                return render(request, 'authentication/register.html')
        return render(request,'authentication/register.html')        
                     
class VerificationView(View):
    def get(self, request,uidb64,token):
        
        try:
            id= force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=id)
            if not token_generator.check_token(user,token):
                return redirect('login'+ '?message'+ 'User already activated.')
            
            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            
            messages.success(request, 'Account Activated successfully.')
            return redirect('login')
        except Exception as ex:
            pass        

        return redirect('login')
    

class LoginView(View):
    def get(self, request):
        return render(request,'authentication/login.html')
    
    def post(self, request):
        username = request.POST['username']    
        password = request.POST['password'] 
        if username and  password:
            user = auth.authenticate(username=username, password=password)
            
            if user:
                if user.is_active:
                    auth.login(request, user) 
                    messages.success(request, 'Welcome, '+user.username+' you are now logged in.')

                    return redirect('expenses')
             
                messages.error(request,'Account is not active,please check your email.' )
                return render(request,'authentication/login.html')
            
            messages.error(request,'Invalid credentials,try again.' )
            return render(request,'authentication/login.html')

        
        messages.error(request,'Please fill all fields.' )
        return render(request,'authentication/login.html')
    
    
class   LogoutView(View):
    def post(self,request): 
        auth.logout(request)
        messages.success(request,'You have been logged out.') 
        return redirect('login') 
    


