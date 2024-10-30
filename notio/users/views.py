from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, UserLoginForm, ProfileForm
from django.contrib.auth.decorators import login_required


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('note_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('note_list')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def profile(request):
    return render(request, 'account/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/profile_update.html', {'form': form})
