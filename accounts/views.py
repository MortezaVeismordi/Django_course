from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout , get_user_model
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages 
from django.contrib.auth.hashers import make_password

#------------------------------------------------------------------------------------------------

def login_view(request):
    if request.method == "POST":
        username_email = request.POST.get("username_email", "").strip()
        password = request.POST.get("password", "").strip()
        if not username_email or not password: 
            messages.error(request, "Please enter username or email and password.")
            return render(request, "accounts/login.html")
        user = None
        if "@" in username_email:
            try:
                user_obj = User.objects.get(email=username_email)  
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                messages.error(request, "No account found with this email.")
                return render(request, "accounts/login.html")
        else:  
            user = authenticate(request, username=username_email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("/")
        else:
            messages.error(request, "Invalid username/email or password.")
    return render(request, "accounts/login.html")

#----------------------------------------------------------------------------------------------------------  

def logout_veiw(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

#----------------------------------------------------------------------------------------------------------

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("accounts:signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("accounts:signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("accounts:signup")

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect("/")

    return render(request, "accounts/signup.html")

#-----------------------------------------------------------------------------------------------------

def forgot_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        old_password = request.POST.get("old_password")
        user = authenticate(request, username=username, password=old_password)
        if user:
            request.session["reset_user"] = user.username  
            return redirect("accounts:reset_password")
        else:
            messages.error(request, "Username or password is incorrect.")

    return render(request, "accounts/forgot.html")

#-------------------------------------------for (reset_password_view) to work last func must been done -------------------------------------

def reset_password_view(request):
    if "reset_user" not in request.session:
        return redirect("accounts:password_reset")
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("accounts:reset_password")

        username = request.session["reset_user"]
        user = get_user_model().objects.get(username=username)
        user.password = make_password(new_password)
        user.save()

        del request.session["reset_user"]
        messages.success(request, "Password has been successfully changed. Please log in.")
        return redirect("accounts:login")

    return render(request, "accounts/reset_password.html")

