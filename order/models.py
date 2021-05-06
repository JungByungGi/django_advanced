from django.db import models


# Create your models here.

class Order(models.Model):
    fcuser = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량') # integerfield : 정수 데이터 저장
    # 기존 데이터들에 대한 memo, status 값은 어떻게 처리할 지 모르기 때문에 default, null과 blank를 넣어줌.
    status = models.CharField(
        #관리자 페이지에서 상태 선택 가능
        choices=(
            ('대기중', '대기중'),
            ('결제대기', '결제대기'),
            ('결제완료', '결제완료'),
            ('환불', '환불'),
        ),
        default='대기중', max_length=32, verbose_name='상태')
    memo = models.TextField(null=True, blank=True, verbose_name='메모')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜') # auto_now_add : 최초 저장 시에만 현재날짜를 적용 / auto_now는 save 할 때마다 현재날짜로 갱신
    
    
    def __str__(self):
        return str(self.fcuser) + ' ' + str(self.product)

    class Meta:
        db_table = 'fastcampus_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
