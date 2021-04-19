from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.edit import FormView


class OrderCreate(FormView):
    # formview를 화면을 보여주는 용도로 쓰지 않기 때문에 템플릿 필요 없음(화면은 상품 상세보기에 이미 있음)
    form_class = RegisterForm
    success_url = '/product/'
    
    # 유효하지 않은 경우 본 페이지로 돌아가기
    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    # 폼 생성 시 어떤 인자값을 전달해서 만들건지 결정하는 함수
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw