from django import forms
from .models import Order
from product.models import Product
from fcuser.models import Fcuser
from django.db import transaction


class RegisterForm(forms.Form):
    # form 안에서 request 전달
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        }, label='수량'
    )
    # 사용자와 제품은 입력을 id로 받을 거기 때문에 int(단, 사용자의 경우는 로그인 시 아이디 값이 전달되어야 하므로 따로 추가할 필요 없음.(session에 저장되어 있음))
    product = forms.IntegerField(
        error_messages={
            'required': '상품을 입력해주세요.'
        }, label='상품', widget=forms.HiddenInput  # 상품명은 조회되는 페이지에 이미 표시되는 값이지 실제로 입력하는 값이 아니므로 hiddenInput widget 사용
    )

    # vaildation
    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        # session에 있는 user 정보를 가지고 옴
        fcuser = self.request.session.get('user')

        if quantity and product and fcuser:
            # 안의 모든 동작이 transaction으로 처리된다.
            # transaction : 모든 동작이 올바르게 수행되어야 실행됨. 가령 주문을 했는데 수량이 줄지 않았다면 rollback함.
            with transaction.atomic():
                prod = Product.objects.get(pk=product)
                order = Order(
                    quantity=quantity,
                    product=Product.objects.get(pk=product),
                    fcuser=Fcuser.objects.get(email=fcuser)
                )
                order.save()
                prod.stock -= quantity
                prod.save()
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')
