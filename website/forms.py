from django import forms
from website.models import Contact

#-----------------------------------------------


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)


#-----------------------------------------------


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        