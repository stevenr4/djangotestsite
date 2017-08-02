# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .models import UserAddress


# The home page
def index(request):
    return render(request, 'index.html')


# The user registration form
def register_user(request):

    # Determine if someone submitted the form or is just hitting the page
    if request.method == 'POST':

        # Since it is a post, get the information
        form = RegistrationForm(request.POST)

        # Make sure the form is valid
        if form.is_valid():

            # Since the form is valid, save the form and capture the object
            useraddress = form.save()

            # Save the user address so that it can be seen on the confirmation
            request.session['useraddress'] = useraddress.id

            # Finally, redirect the user to the confirmation page
            return redirect('confirmation')
    else:
        # Since the method was not a post, let's make a new post to send
        form = RegistrationForm()

    # Render the page and send the form to the user
    return render(request, 'register_user.html', {'form': form})


# The page that a user is redirected to after they register
def confirmation(request):

    # Get the user's most recently registered address
    ua = UserAddress.objects.get(pk=request.session['useraddress'])

    # I realize it's possible for a user to hit this page
    #   without registering and it could cause problems.
    # If this were a serious app, I would keep an eye out and
    #   handle all those odd scenarios

    # Render the address back to the user
    return render(request, 'confirmation.html', {'useraddress': ua})
