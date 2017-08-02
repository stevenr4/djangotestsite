# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm



def index(request):
    return HttpResponse("Todo: MAIN PAGE")


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            useraddress = form.save()

            # Normally I would login the user once they successfully created their profile or send an email verification
            # but since we are only collecting data, I am just going to redirect the user to the confirmation page
            return redirect('confirmation')
    else:
        form = RegistrationForm()
    return render(request, 'register_user.html', {'form': form})


def confirmation(request):
    return HttpResponse("TODO: Confirmation Page")
