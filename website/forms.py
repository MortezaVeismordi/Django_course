from django import forms
from website.models import Contact
from captcha.fields import CaptchaField
#-----------------------------------------------


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)


#-----------------------------------------------


class ContactForm(forms.ModelForm):
    # subject = forms.CharField(required=False)
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']
        
        