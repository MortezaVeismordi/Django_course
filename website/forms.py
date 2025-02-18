from django import forms
from website.models import Contact

#-----------------------------------------------


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)


#-----------------------------------------------


class ContactForm(forms.ModelForm):
    subject = forms.CharField(required=False)
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']
        
        