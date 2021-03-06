from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.edit import FormView
from fcuser.decorators import login_required
from django.utils.decorators import method_decorator  # 장고에서 class에 decorator를 사용할 수 있도록 제공해주는 함수
from django.views.generic import ListView
from django.db import transaction
from .models import Order
from product.models import Product
from fcuser.models import Fcuser


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    # formview를 화면을 보여주는 용도로 쓰지 않기 때문에 템플릿 필요 없음(화면은 상품 상세보기에 이미 있음)
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity=form.data.get('quantity'),
                product=Product.objects.get(pk=form.data.get('product')),
                #user는 session에서 가져옴
                fcuser=Fcuser.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()

        return super().form_valid(form)

    # 유효하지 않은 경우 본 페이지로 돌아가기
    def form_invalid(self, form):
        return redirect('/product/' + str(form.product.get('product')))

    # 폼 생성 시 어떤 인자값을 전달해서 만들건지 결정하는 함수
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


# 리스트 뷰를 이용해 상품목록 조회
@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    # 다른 사람이 주문한 정보도 보여짐
    # model = Order

    template_name = 'order.html'
    context_object_name = 'order_list'

    # 따라서 함수 오버라이딩을 통해 queryset을 만들어 로그인한 사용자의 주문 정보만 볼 수 있도록 한다.
    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset

