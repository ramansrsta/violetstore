from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from .models import AddProductModel

USER = get_user_model()


class AdminAddForm(ModelForm):
    class Meta:
        model = USER
        fields = ['first_name','last_name','username','password']
        widgets = {
            'password' : forms.PasswordInput()
        }

#create using forms.Form
class AdminLoginFrom(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150,widget=forms.PasswordInput())


class AddProductForm(ModelForm):
    class Meta:
        model = AddProductModel
        fields = ['product_name','product_description','product_image','price']
        widgets={
            'product_name' : forms.TextInput(attrs={'placeholder': 'name'}),
            'product_description': forms.TextInput(attrs={'placeholder':'description'})
        }

    