from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
# Create your views here.


# 리스트 뷰를 이용해 상품목록 조회
class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    # html file에서 object_list 이름을 바꾸고 싶을 때 사용
    context_object_name = 'product_list'


class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'