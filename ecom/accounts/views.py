from django.shortcuts import render, redirect
from django.views.generic import TemplateView,CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import AdminAddForm, AdminLoginFrom, AddProductForm
from .models import AddProductModel

from frontend.models import OrderProduct
from frontend.forms import OrderProductForm

USER = get_user_model()


# Create your views here. Admin Operations Starts From Here
class AddAdminView(CreateView):
    def get(self,request,*args,**kwargs):
        form = AdminAddForm()
        return render(request, 'accounts/register.html',{ 'form': form })

    def post(self,request,*args,**kwargs):
        form = AdminAddForm(request.POST)
        if form.is_valid():
            print('form is clean')
            print(form.cleaned_data)
            user = USER(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                )    
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/accounts/login/')
        else:
            return render(request, 'accounts/register.html',{ 'form': form })

@method_decorator(login_required,name='dispatch')
class HomePageView(TemplateView):
    template_name = 'accounts/homepage.html'

#soultion dont use modelform in this use form.form in this very matter
def login_view(request):
    if request.method == 'POST':
        form = AdminLoginFrom(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                )
            if user:
                login(request,user)
                return redirect('/accounts/homepage/')
            else:
                print('Username or password doesnot exitst')
    elif request.method == 'GET':
        form = AdminLoginFrom()
    return render(request,'accounts/login.html',{'form':form})

#creating logout view
class AdminLogoutView(LogoutView):
    next_page = '/accounts/login/'

@method_decorator(login_required, name='dispatch')
class AdminsList(ListView):
    model = USER
    template_name = 'accounts/adminList.html'
    context_object_name = 'admin_data'

@method_decorator(login_required,name='dispatch')
class UpdateAdmin(UpdateView):
    model = USER
    template_name = 'accounts/update.html'
    form_class = AdminAddForm
    context_object_name = 'admin_data'
    success_url = reverse_lazy('accounts:list')

@method_decorator(login_required,name='dispatch')
class DeleteAdmin(DeleteView):
    model = USER
    success_url = reverse_lazy('accounts:list')

###Products Operation Starts From Here
@method_decorator(login_required,name='dispatch')
class AddProduct(CreateView):
    model = AddProductModel
    form_class = AddProductForm
    template_name = 'accounts/addProduct.html'

    def form_valid(self,form):
        product = form.save(commit=False)
        product.product_added_by = self.request.user
        product.save()
        return redirect('/accounts/viewProduct/')


@method_decorator(login_required, name='dispatch')
class ProductView(ListView):
    model = AddProductModel
    template_name = 'accounts/viewProduct.html'
    context_object_name = 'product_data'

@method_decorator(login_required,name='dispatch')
class UpdateProduct(UpdateView):
    model = AddProductModel
    template_name = 'accounts/editProduct.html'
    form_class = AddProductForm
    success_url = reverse_lazy('accounts:viewProduct')

@method_decorator(login_required,name='dispatch')
class DeleteProduct(DeleteView):
    model = AddProductModel
    success_url = reverse_lazy('accounts:viewProduct')

@method_decorator(login_required, name='dispatch')
class OrderView(ListView):
    model = OrderProduct
    template_name = 'accounts/viewOrders.html'
    context_object_name = 'order_data'

@method_decorator(login_required,name='dispatch')
class UpdateOder(UpdateView):
    model = OrderProduct
    form_class = OrderProductForm
    template_name = 'accounts/editOrders.html'
    success_url = reverse_lazy('accounts:viewOrder')

    def form_valid(self,form):
        order = form.save(commit=False)
        order.checked_by = self.request.user.first_name
        order.save()
        return redirect('/accounts/viewOrder/')







           
  
    
