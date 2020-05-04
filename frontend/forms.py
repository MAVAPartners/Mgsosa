from django import forms

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