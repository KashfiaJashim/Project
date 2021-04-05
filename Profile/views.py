from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # we can use all messages from 'messages' framework
from django.contrib.auth.decorators import login_required


# Create your views here.

def showHome(request):
    return render(request, 'Homepage/ShowHome.html')


# user_registration.

def registration(request):
    user_form = UserCreationForm()
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Account is created successfully')

    context = {
        'form': user_form,
    }

    return render(request, 'profile/registration.html', context)


# create_Profile

@login_required
def createprofile(request):
    form = ProfileForm()

    message = ""
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        message = "Invalid input. Please try again later."
        if form.is_valid():
            profile = form.save(commit=False)

            profile.user = request.user

            profile.save()

            message = "Profile is Created "
            form = ProfileForm()
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'profile/CreateProfile.html', context)


# show_Profile

@login_required
def showProfile(request):
    profile = Profile.objects.filter(user=request.user)

    if len(profile) != 0:
        p = profile[0]
    else:
        p = "No Profile"

    context = {
        'profile': p

    }

    return render(request, 'Profile/ShowProfile.html', context)
