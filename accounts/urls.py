from django.urls import path
from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    #login
    path('login/' , login_view , name='login'),
    path('forgot/' , forgot_view , name='forgot'),
    path('reset-password/', reset_password_view, name='reset_password'),
    #logout
    path('logout/' , logout_veiw , name="logout"),
    # registe/signup
    path('signup/' , signup_view , name='signup')

]