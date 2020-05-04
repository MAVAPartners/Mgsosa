from django.shortcuts import render
import requests
from datetime import datetime
import json
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages

from .forms import ContactForm


# Create your views here.

EMAIL_SUBJECT = 'From MGSOSA website'
# TO_EMAIL = 'mava.partnersin@gmail.com,anoob.vm@mavapartners.com'

TO_EMAIL = 'mava.partnersin@gmail.com'
# TO_EMAIL = 'anoob.vm@mavapartners.com'


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
        else:
            prayer = 'May God Bless You'
    else:
        prayer = 'May God Bless You'
    return render(request, 'home-sample.html', {'prayer': prayer})

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
            return home(request)
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
        else:
            prayer = 'May God Bless You'
    else:
        prayer = 'May God Bless You'
    return render(request, 'home-sample.html', {'prayer': prayer})

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
        else:
            prayer = 'May God Bless You'
    else:
        prayer = 'May God Bless You'
    return render(request, 'home-sample-two.html', {'prayer': prayer})