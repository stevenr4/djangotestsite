from django import forms

from .models import UserAddress


# This is the form that the user will fill out to register
class RegistrationForm(forms.ModelForm):

    # Address data for the user
    first_name = forms.CharField(max_length=127, label="Your First Name")
    last_name = forms.CharField(max_length=127, label="Your Last Name")
    address_1 = forms.CharField(max_length=127, label="Address Line 1")
    address_2 = forms.CharField(max_length=127, label="Address Line 2", required=False)
    city = forms.CharField(max_length=127, label="City")
    state = forms.ChoiceField(label="State", choices=UserAddress.STATE_CHOICES)
    country = forms.CharField(max_length=2, label="Country",
                              initial="US", disabled=True)

    class Meta:
        model = UserAddress
        fields = (
            'first_name',
            'last_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'country'
        )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['address_2'].required = False
