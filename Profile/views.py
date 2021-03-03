from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile
# Create your views here.

def showHome(request):
    return render(request, 'homepage.html')

#user_registration.

def registration(request):
    user_form = UserCreationForm()
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Account is created successfully')

    context = {
        'user_form': user_form,
    }

    return render(request,'profile/registration.html', context)

