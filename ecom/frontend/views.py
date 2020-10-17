from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import hashers
from django.views import View
from django.db.models import Avg, Count, Min, Sum

from .models import ClientRegister, ClientLogin, CartCreator, OrderProduct
from .forms import ClientRegisterForm, ClientLoginForm, CartCreatorForm, OrderProductForm

from accounts.models import AddProductModel

# Create your views here.
class IndexPage(TemplateView):
    template_name = 'frontend/index.html'

class CategoriesPage(ListView):
    model = AddProductModel
    template_name = 'frontend/categories.html'
    context_object_name = 'product_data'

class CheckOutPage(ListView):
    model = CartCreator
    template_name = 'frontend/check-out.html'
    context_object_name = 'cart_info'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderProductForm()  
        context['total'] =  CartCreator.objects.filter(client_id=self.request.session['client_id']).aggregate(Sum('total_price'))
        return context

class OrderComplete(CreateView):
    model = OrderProduct
    form_class = OrderProductForm
    template_name = 'frontend/check-out.html'
  
    def form_valid(self,form):
        total = CartCreator.objects.filter(client_id=self.request.session['client_id']).aggregate(Sum('total_price'))
        order = form.save(commit=False)
        order.client_id = self.request.session['client_id']
        order.payable_amount = total['total_price__sum']
        order.save()
        objects = CartCreator.objects.filter(client_id=self.request.session['client_id'])
        objects.delete()
        return redirect('frontend:categories')


class ContactPage(TemplateView):
    template_name = 'frontend/contact.html'

class ProductPage(DetailView):
    model = AddProductModel
    template_name = 'frontend/product-page.html'
    context_object_name = 'product_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartCreatorForm()
        return context

class ShoppingCart(ListView):
    model = CartCreator
    template_name = 'frontend/shopping-cart.html'
    context_object_name = 'cart_data'

class RegisterClient(CreateView):
    model = ClientRegister
    form_class = ClientRegisterForm
    template_name = 'frontend/register.html'

    def form_valid(self,form):
        print(form.data)
        print(form.cleaned_data['password'])
        client = form.save(commit=False)
        client.password = form.cleaned_data['password'] #correct way of manipulation of form data
        print(form.data)
        client.save()
        return redirect('frontend:login')


def login_client(request):
    if request.method == 'POST':
        form = ClientLoginForm(request.POST)
        print(form.data)
        email = form.data['email']
        password = form.data['password']
        clientData = ClientRegister.objects.get(email=email)
        if form.is_valid():
            if password == clientData.password and email == clientData.email:
                request.session['email'] = email
                request.session['client_id'] = clientData.id
                return redirect('frontend:index')
            else:
                print('Error fucking error')
    elif request.method == 'GET':
        form = ClientLoginForm()
    return render(request,'frontend/login.html',{'form':form})


class CartCreatorView(CreateView):
    model = CartCreator
    form_class = CartCreatorForm
    template_name = 'frontend/product-page.html'
    success_url = reverse_lazy('frontend:categories')

    def form_valid(self,form):
        cart_data = form.save(commit=False)
        cart_data.product_id =  self.kwargs['pk']
        cart_data.client_id = self.request.session['client_id']

        product_info = AddProductModel.objects.get(id=cart_data.product_id)
        cart_data.total_price = int(cart_data.product_count) * int(product_info.price)

        print(cart_data.product_count) #gives number of products
        print(cart_data.product_id) #gives id of product 
        print(cart_data.client_id) #gives id of client
        print(cart_data.total_price) #gives total price 

        cart_data.save()
        return super(CartCreatorView, self).form_valid(form)


class PostCommentView(View):
    def get(self, request, *args, **kwargs):
         view = ProductPage.as_view()
         return view(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs) :
         view = CartCreatorView.as_view()
         return view(request, *args, **kwargs) 


class CartRemoverView(DeleteView):
    model = CartCreator
    success_url = reverse_lazy('frontend:cart')

class Odr(View):
    def get(self, request, *args, **kwargs):
         view = CheckOutPage.as_view()
         return view(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs) :
         view = OrderComplete.as_view()
         return view(request, *args, **kwargs) 



        









    