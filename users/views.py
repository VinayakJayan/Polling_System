from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .forms import UserUpdateForm, ProfileUpdateForm, UpdatePasswords
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import reverse
from django.views.generic import RedirectView


def register(request):
    if request.method == "POST":  # Handle POST request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get(
                "username"
            )  # Get the username from the form
            messages.success(request, f"Account created for {username}!")
            return redirect(
                "login"
            )  # Redirect to login page after successful registration
    else:  # Handle GET request, create an empty form
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == 'POST':   
        u_form = UserUpdateForm(request.POST, instance=request.user)  
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = { 
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def change_password(request):
    context = {'form':''}
    if request.method == 'POST':
        form = UpdatePasswords(user = request.user, data= request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Account Password has been updated successfully")
            update_session_auth_hash(request, form.user)
        context['form'] = form
    else:
        form = UpdatePasswords(request.POST)
        context['form'] = form
    return render(request,'users/change_password.html',context)


class CustomLogoutView(RedirectView):
    url = "/login/"  # Redirect URL after logout

    def get_redirect_url(self, *args, **kwargs):
        # Add custom logic here if needed
        return super().get_redirect_url(*args, **kwargs)
    
@login_required
def update_profile(request):
    if request.method == 'POST':   
        u_form = UserUpdateForm(request.POST, instance=request.user)  
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = { 
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update_profile.html', context)
