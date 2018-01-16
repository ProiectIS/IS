from django import forms

from django.contrib.auth.models import User  # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm
from .models import Order

#unit testing -> proiect!!!!!

class RegistrationForm(UserCreationForm):  #extend UserCreationForm and add extra funct
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()

        return user

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city','phone']


# --------
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
