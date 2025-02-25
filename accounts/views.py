from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings

# -----------------------------------------------------------------------------------------------------

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
                user = authenticate(
                    request, username=user_obj.username, password=password
                )
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

# ----------------------------------------------------------------------------------------------------------

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")

# ----------------------------------------------------------------------------------------------------------

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        email = request.POST.get("email").strip()
        password1 = request.POST.get("password1").strip()
        password2 = request.POST.get("password2").strip()

        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect("accounts:signup")
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("accounts:signup")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("accounts:signup")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("accounts:signup")
        user = User.objects.create_user(
            username=username, email=email, password=password1
        )
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect("/")

    return render(request, "accounts/signup.html")

# -----------------------------------------------------------------------------------------------------

def forgot_view(request):
    if request.method == "POST":
        email = request.POST.get("email").strip()

        if not email:
            messages.error(request, "Please enter your email address.")
            return redirect("accounts:forgot")

        try:
            user = User.objects.get(email=email)

            token = get_random_string(length=32)
            request.session["reset_token"] = token
            request.session["reset_email"] = user.email


            reset_link = request.build_absolute_uri(f"/accounts/reset-password/?token={token}")

            subject = "Reset Your Password"
            message = f"Click the link to reset your password: {reset_link}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

            messages.success(request, "A password reset link has been sent to your email.")
            return redirect("accounts:login")

        except User.DoesNotExist:
            messages.error(request, "No account found with this email.")

    return render(request, "accounts/forgot.html")

# -----------------------------------------------------------------------------------------------------

def reset_password_view(request):
    token = request.GET.get("token")  

    if not token or request.session.get("reset_token") != token:
        messages.error(request, "Invalid or expired token.")
        return redirect("accounts:forgot")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect(f"accounts/reset-password/?token={token}")

        email = request.session.get("reset_email")
        try:
            user = get_user_model().objects.get(email=email)
            user.set_password(new_password)  
            user.save()


            del request.session["reset_token"]
            del request.session["reset_email"]

            messages.success(request, "Your password has been successfully changed. Please log in.")
            return redirect("accounts:login")

        except get_user_model().DoesNotExist:
            messages.error(request, "Something went wrong. Please try again.")
            return redirect("accounts:forgot")

    return render(request, "accounts/reset_password.html")
