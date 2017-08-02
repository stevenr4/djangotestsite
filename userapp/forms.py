from django import forms

from .models import UserAddress


class RegistrationForm(forms.ModelForm):

    # Address data for the user
    firstname = forms.CharField(max_length=127, label="Your First Name")
    lastname = forms.CharField(max_length=127, label="Your Last Name")
    address1 = forms.CharField(max_length=127, label="Address Line 1")
    address2 = forms.CharField(max_length=127, label="Address Line 2")
    city = forms.CharField(max_length=127, label="City")
    state = forms.ChoiceField(label="State", choices=UserAddress.STATE_CHOICES)
    country = forms.CharField(max_length=2, label="Country", initial="US", disabled=True)

    class Meta:
        model = UserAddress
        fields = ('firstname', 'lastname', 'address1', 'address2', 'city', 'state', 'country')
