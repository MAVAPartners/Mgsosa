import json
from datetime import datetime

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext

from .forms import ContactForm, LoginForm, RegistrationForm

# Create your views here.

EMAIL_SUBJECT = 'From MGSOSA website'
# TO_EMAIL = 'mava.partnersin@gmail.com,anoob.vm@mavapartners.com'

TO_EMAIL = 'mava.partnersin@gmail.com'
#TO_EMAIL = 'anoob.vm@mavapartners.com'


def home(request):
    now = datetime.now()
    cur_time = now.strftime("%d %B %Y %H:%M:%S")
    url = 'https://pg-app-cwmbz0wd7eqrjvx5cr32ftd4gsdp3j.scalabl.cloud/1/functions/getPrayers'
    header = {'Content-Type' : 'application/json','X-Parse-Application-Id' : 'AcHG0EJiXqflSC7NbZ5PYtod4mSBfy7u0MqBjj0Z' , 'X-Parse-REST-API-Key' : 'Puqq9HpXVf0WUkBbHXNX8hwybv88xejYepluuUap' }
    myobj = {'prayerType' : 'C', 'translation': 'O', 'currentDate' : cur_time, 'versification' : 'P', 'form' : 'R', 'season' : 'S', 'language' : 'en'}
    response = requests.post(url, json = myobj , headers=header)
    data = response.content.decode('utf-8')
    json_data = json.loads(data)
    if json_data["result"] != '':
        dict = json_data["result"]
        json_data = json.loads(dict)
        if json_data["status"] == 200:
            results = json_data["result"]
            prayer = results[0]['Name']
            prayerurl = results[0]['Prayer']['url']
        else:
            prayer = 'May God Bless You'
            prayerurl = '#'
    else:
        prayer = 'May God Bless You'
        prayerurl = '#'
    return render(request, 'home-sample.html', {'prayer': prayer, 'prayerurl': prayerurl})

def about(request):
    return render(request, 'about.html')

def events(request):
    return render(request, 'event.html')

def all_events(request):
    return render(request, 'events-all.html')

def donations(request):
    return render(request, 'donations.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact.html',{'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']

            message_body = "Hello, \nFollowing message was received from the MGSOSA website: \n"
            message_body = message_body + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n"
            message_body = message_body + "Name: " + name + '\n'
            message_body = message_body + "Email: " + from_email + '\n'
            message_body = message_body + "Phone: " + str(mobile) + '\n'
            message_body = message_body + "Message: " + message + '\n'
            message_body = message_body + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n "
            message_body = message_body + "When we pray with a heart full of devotion, God accepts it and we receive it back in the form of a blessing!\n\n"

            message_body = message_body + "Powered by Team MAVA" +'\n'


            print(name, from_email, mobile, message)

            try:

                send_mail(EMAIL_SUBJECT, message_body, from_email, TO_EMAIL.split(","))
                                                                    # ,anoob.vm@mavapartners.com
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return contact(request)
            messages.success(request, 'Thank you for your message. We will contact you in couple of days. ')
            return HttpResponseRedirect('/contact/')
            # return  render(request, 'contact.html',{'form': form})
        else:
            print('form is NOT valid')
            messages.warning(request, 'Please enter valid data for all the fields including Email address.')
            return render(request, "contact.html", {'form': form})
    return home(request)

def qleedo(request):
    return render(request, 'qleedo.html')

def community(request):
    return render(request, 'community.html')

def dailyPrayer(request):
    now = datetime.now()
    cur_time = now.strftime("%d %B %Y %H:%M:%S")
    url = 'https://pg-app-cwmbz0wd7eqrjvx5cr32ftd4gsdp3j.scalabl.cloud/1/functions/getPrayers'
    header = {'Content-Type' : 'application/json','X-Parse-Application-Id' : 'AcHG0EJiXqflSC7NbZ5PYtod4mSBfy7u0MqBjj0Z' , 'X-Parse-REST-API-Key' : 'Puqq9HpXVf0WUkBbHXNX8hwybv88xejYepluuUap' }
    myobj = {'prayerType' : 'C', 'translation': 'O', 'currentDate' : cur_time, 'versification' : 'P', 'form' : 'R', 'season' : 'S', 'language' : 'en'}
    response = requests.post(url, json = myobj , headers=header)
    data = response.content.decode('utf-8')
    json_data = json.loads(data)
    if json_data["result"] != '':
        dict = json_data["result"]
        json_data = json.loads(dict)
        if json_data["status"] == 200:
            results = json_data["result"]
            prayerUrl = results[0]['Prayer']['url']
        else:
            prayerUrl = '#'
    else:
        prayerUrl = '#'
    return render(request, 'daily-prayer.html', {'prayerUrl':prayerUrl})

def home_sample(request):
    now = datetime.now()
    cur_time = now.strftime("%d %B %Y %H:%M:%S")
    url = 'https://pg-app-cwmbz0wd7eqrjvx5cr32ftd4gsdp3j.scalabl.cloud/1/functions/getPrayers'
    header = {'Content-Type' : 'application/json','X-Parse-Application-Id' : 'AcHG0EJiXqflSC7NbZ5PYtod4mSBfy7u0MqBjj0Z' , 'X-Parse-REST-API-Key' : 'Puqq9HpXVf0WUkBbHXNX8hwybv88xejYepluuUap' }
    myobj = {'prayerType' : 'C', 'translation': 'O', 'currentDate' : cur_time, 'versification' : 'P', 'form' : 'R', 'season' : 'S', 'language' : 'en'}
    response = requests.post(url, json = myobj , headers=header)
    data = response.content.decode('utf-8')
    json_data = json.loads(data)
    if json_data["result"] != '':
        dict = json_data["result"]
        json_data = json.loads(dict)
        if json_data["status"] == 200:
            results = json_data["result"]
            prayer = results[0]['Name']
            prayerurl = results[0]['Prayer']['url']
        else:
            prayer = 'May God Bless You'
            prayerurl = '#'
    else:
        prayer = 'May God Bless You'
        prayerurl = '#'
    return render(request, 'home-sample.html', {'prayer': prayer, 'prayerurl': prayerurl})

def home_sample_two(request):
    now = datetime.now()
    cur_time = now.strftime("%d %B %Y %H:%M:%S")
    url = 'https://pg-app-cwmbz0wd7eqrjvx5cr32ftd4gsdp3j.scalabl.cloud/1/functions/getPrayers'
    header = {'Content-Type' : 'application/json','X-Parse-Application-Id' : 'AcHG0EJiXqflSC7NbZ5PYtod4mSBfy7u0MqBjj0Z' , 'X-Parse-REST-API-Key' : 'Puqq9HpXVf0WUkBbHXNX8hwybv88xejYepluuUap' }
    myobj = {'prayerType' : 'C', 'translation': 'O', 'currentDate' : cur_time, 'versification' : 'P', 'form' : 'R', 'season' : 'S', 'language' : 'en'}
    response = requests.post(url, json = myobj , headers=header)
    data = response.content.decode('utf-8')
    json_data = json.loads(data)
    if json_data["result"] != '':
        dict = json_data["result"]
        json_data = json.loads(dict)
        if json_data["status"] == 200:
            results = json_data["result"]
            prayer = results[0]['Name']
            prayerurl = results[0]['Prayer']['url']
        else:
            prayer = 'May God Bless You'
            prayerurl = '#'
    else:
        prayer = 'May God Bless You'
        prayerurl = '#'
    return render(request, 'home-sample-two.html', {'prayer': prayer, 'prayerurl': prayerurl})


def event_details(request):
    return render(request, 'event-details.html')

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        print('....registration_view.......');
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user.is_active = True
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            #account = authenticate(email=email, password=password1)
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            form = RegistrationForm()
            context['registration_form'] = form
            messages.success(request, 'User Signup successfully Please contact Administrator for approval')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'signup.html', context)


def login_user(request):
    context = {}
    if request.POST:
        form = AuthenticationForm(request, data=request.POST)
        #print('.....form AuthenticationForm.... '+request.POST['username'])
        #username = form.cleaned_data['username']
        #password = form.cleaned_data['password']
        username = request.POST['username']
        password = request.POST['password']
        print(password+'..r...form AuthenticationForm....55... '+username)


        #user = auth_login(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                userData = login(request, user)
                if userData is not None:
                    messages.success(request, 'You are now successfully loged in')
                    return HttpResponseRedirect('/forum/')
                else:
                    messages.error(request, 'Please request Admin to approve this user authentication')
                    context['login_form'] = form
            else:
                messages.error(request, 'Invalid username / password')
                context['login_form'] = form
        else:
            messages.error(request, 'Invalid username / password')
            context['login_form'] = form
    else:
        form = AuthenticationForm()
        context['login_form'] = form
    return render(request, 'login.html', context)

def logout_request(request):
    logout(request)
    messages.success(request, 'You are now successfully logged out')
    return HttpResponseRedirect('/signin/')
