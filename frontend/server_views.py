import json
from datetime import datetime

import requests
from django.contrib import messages
from django.contrib.auth import authenticate as auth_login
from django.contrib.auth import login as login_default
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, EmailMultiAlternatives, send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import Context, RequestContext
from django.template.loader import render_to_string

from .forms import ContactForm, LoginForm, RegistrationForm

# Create your views here.

EMAIL_SUBJECT = 'From MGSOSA website'
# TO_EMAIL = 'mava.partnersin@gmail.com,anoob.vm@mavapartners.com'

#TO_EMAIL = 'mava.partnersin@gmail.com'
TO_EMAIL = 'contactus@mgsosa.com'


def home(request):
    return render(request, 'home-sample.html', {'prayer': '', 'prayerurl': ''})


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
        return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']

            message_body = "Hello, \nFollowing message was received from the MGSOSA website: \n"
            message_body = message_body + \
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n"
            message_body = message_body + "Name: " + name + '\n'
            message_body = message_body + "Email: " + from_email + '\n'
            message_body = message_body + "Phone: " + str(mobile) + '\n'
            message_body = message_body + "Message: " + message + '\n'
            message_body = message_body + \
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n "
            message_body = message_body + \
                "When we pray with a heart full of devotion, God accepts it and we receive it back in the form of a blessing!\n\n"

            message_body = message_body + "Powered by Team MAVA" + '\n'

            print(name, from_email, mobile, message)

            try:

                send_mail(EMAIL_SUBJECT, message_body,
                          from_email, TO_EMAIL.split(","))
                # ,anoob.vm@mavapartners.com
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return contact(request)
            messages.success(
                request, 'Thank you for your message. We will contact you in couple of days. ')
            return HttpResponseRedirect('/contact/')
            # return  render(request, 'contact.html',{'form': form})
        else:
            print('form is NOT valid')
            messages.warning(
                request, 'Please enter valid data for all the fields including Email address.')
            return render(request, "contact.html", {'form': form})
    return home(request)


def qleedo(request):
    return render(request, 'qleedo.html')


def community(request):
    return render(request, 'community.html')


def dailyPrayer(request):
    return render(request, 'daily-prayer.html', {'detailsUrl': 'url'})


def home_sample(request):
    try:
        now = datetime.now()
        cur_time = now.strftime("%d %B %Y %H:%M:%S")
        url = 'https://pg-app-cwmbz0wd7eqrjvx5cr32ftd4gsdp3j.scalabl.cloud/1/functions/getPrayers'
        header = {'Content-Type': 'application/json', 'X-Parse-Application-Id': 'AcHG0EJiXqflSC7NbZ5PYtod4mSBfy7u0MqBjj0Z',
                'X-Parse-REST-API-Key': 'Puqq9HpXVf0WUkBbHXNX8hwybv88xejYepluuUap'}
        myobj = {'prayerType': 'C', 'translation': 'O', 'currentDate': cur_time,
                'versification': 'P', 'form': 'R', 'season': 'S', 'language': 'en'}
        response = requests.post(url, json=myobj, headers=header)
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
    except Exception as e:
            print(e)
            prayer = 'May God Bless You'
            prayerurl = '#'
    return render(request, 'home-sample.html', {'prayer': prayer, 'prayerurl': prayerurl})


def home_sample_two(request):
    now = datetime.now()
    cur_time = now.strftime("%d %B %Y %H:%M:%S")
    url = 'https://pg-app-cwmbz0wd7eqrjvx5cr32ftd4gsdp3j.scalabl.cloud/1/functions/getPrayers'
    header = {'Content-Type': 'application/json', 'X-Parse-Application-Id': 'AcHG0EJiXqflSC7NbZ5PYtod4mSBfy7u0MqBjj0Z',
              'X-Parse-REST-API-Key': 'Puqq9HpXVf0WUkBbHXNX8hwybv88xejYepluuUap'}
    myobj = {'prayerType': 'C', 'translation': 'O', 'currentDate': cur_time,
             'versification': 'P', 'form': 'R', 'season': 'S', 'language': 'en'}
    response = requests.post(url, json=myobj, headers=header)
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
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            useremail = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user.is_active = True
            user.email = useremail
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            #account = authenticate(email=email, password=password1)
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            superusers_emails = User.objects.filter(
                is_superuser=True).values('email')
            toEmail = []
            for email in superusers_emails:
                adminEmail = email['email']
                if adminEmail:
                    toEmail.append(adminEmail)

            # send email
            html_content = '<html><body style="color:black;font-weight:400;font-size:20px " ><h4 style="font-weight:400;">Hello,</h4>\n<h4 style="font-weight:400;" >Following message was received from the MGSOSA website:</h2><h4 style="font-weight:400;">New user signup in the system, please verify the user by visiting the admin portal.</h4><a style="font-weight:200;" href="http://mgsosa-staging.mavapartners.com/admin">Admin Portal</a> <br><h4 style="font-weight:200;">Name: ' + \
                first_name + ' ' + last_name + '</h4><h4 style="font-weight:200;">Email: ' + useremail + \
                '</h4><br><h5 style="color:#7f5604">When we pray with a heart full of devotion, God accepts it and we receive it back in the form of a blessing!</h5><h5 style="color:#7f5604;text-align: center;">Powered by Team MAVA</h5></body></html>'
            try:
                # to email for production is TO_EMAIL
                # in staging toEmail
                msg = EmailMultiAlternatives(
                    EMAIL_SUBJECT, '', TO_EMAIL, TO_EMAIL.split(","))
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                print(useremail, toEmail)
                form = RegistrationForm()
                context['registration_form'] = form
                messages.success(
                    request, 'User Signup successfully Please contact Administrator for approval')
                #send_mail(EMAIL_SUBJECT, message_body,TO_EMAIL, toEmail)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                print('...superusers_emails.,,,,,,Exception.', e)
                context['registration_form'] = form
                messages.error(request, e)
                return HttpResponse('Invalid header found.')
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

        #
        #user = authenticate(username=username, password=password)
        # print(user)
        if form.is_valid():
            authUser = auth_login(
                request, username=username, password=password)
            if authUser is not None:
                userData = login_default(
                    request, authUser)
                if request.user.is_superuser:
                    messages.success(
                        request, 'You are now successfully loged in')
                    return HttpResponseRedirect('/forum/')
                elif request.user.is_staff:
                    messages.success(
                        request, 'You are now successfully loged in')
                    return HttpResponseRedirect('/forum/')
                else:
                    logout(request)
                    messages.error(
                        request, 'Please request Admin to approve this user authentication')
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
    return HttpResponseRedirect('/login/')
