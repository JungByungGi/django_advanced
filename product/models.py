from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품 설명')  # charfield와는 다르게 문자열 길이 제한이 없음
    stock = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜') # auto_now_add : 최초 저장 시에만 현재날짜를 적용 / auto_now는 save 할 때마다 현재날짜로 갱신

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fastcampus_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'