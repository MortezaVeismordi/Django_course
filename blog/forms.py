from django import forms
from blog.models import Coment
from captcha.fields import CaptchaField

#--------------------------------------------------

class CommentForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Coment
        fields = ['post','name', 'subject', 'email', 'message']