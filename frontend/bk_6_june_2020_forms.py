from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
	name = forms.CharField(required=True,max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }
        ))
	email = forms.EmailField(required=True, max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

	mobile = forms.IntegerField(required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
        help_text='Write here your message!')

	message = forms.CharField(required=True,max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        help_text='Write here your message!' )


	def clean(self):
	    cleaned_data = super(ContactForm, self).clean()
	    name = cleaned_data.get('name')
	    email = cleaned_data.get('email')
	    mobile = cleaned_data.get('mobile')
	    message = cleaned_data.get('message')
	    if not name and not email and not message:
	        raise forms.ValidationError('You have to write something!')




class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Required. A vallid email address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	username = forms.CharField(help_text='Required. A User Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
	password1 = forms.CharField(help_text='Required. Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	password2 = forms.CharField(help_text='Required. Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	first_name = forms.CharField(help_text='Required. First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(help_text='Required. Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

class Meta:
    model = User
    fields = ("email", "username", "password1", "password2", "first_name", "last_name")



class LoginForm(AuthenticationForm):
	username = forms.CharField(help_text='Required. A User Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
	password = forms.CharField(help_text='Required. Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
