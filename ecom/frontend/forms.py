from django import forms
from django.forms import ModelForm

from .models import ClientRegister, ClientLogin, CartCreator, OrderProduct

#create your forms here
class ClientRegisterForm(ModelForm):
    class Meta:
        model = ClientRegister
        fields = ['first_name','last_name','email','password']
        widgets={
            'first_name' : forms.TextInput(attrs={'placeholder': 'firstname'}),
            'last_name': forms.TextInput(attrs={'placeholder':'lastname'}),
            'email' : forms.TextInput(attrs={'placeholder': 'e@gmail.com'}),
            'password' : forms.PasswordInput(attrs={'placeholder': 'Password from numbers and letters of the Latin alphabet'})
        }
        labels = {
        'first_name': '',
        'last_name' : '',
        'email': '',
        'password': ''
        }

class ClientLoginForm(ModelForm):
    class Meta:
        model = ClientLogin
        fields = ['email','password']
        widgets = {
            'email' : forms.TextInput(attrs={'placeholder' :'Email Input'}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'Input Password'})
        }
        label = {
            'email' : '',
            'password' : ''
        }

class CartCreatorForm(ModelForm):
    product_count = forms.CharField(initial=1) 
    class Meta:
        model = CartCreator
        fields = ['product_count']
        label = {
            'product_count' : ''
        }


class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['first_name','last_name','email']
        labels = {
        'first_name': '',
        'last_name' : '',
        'email': '',
        }
        widgets={
            'first_name' : forms.TextInput(attrs={'placeholder': 'firstname'}),
            'last_name': forms.TextInput(attrs={'placeholder':'lastname'}),
            'email' : forms.TextInput(attrs={'placeholder': 'e@gmail.com'}),
        }