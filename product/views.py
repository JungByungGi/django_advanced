from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from fcuser.decorators import admin_required
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm


# Create your views here.


# 리스트 뷰를 이용해 상품목록 조회
class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    # html file에서 object_list 이름을 바꾸고 싶을 때 사용
    context_object_name = 'product_list'


@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product=Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    # form에 data 전달하는 함수
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
