from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # 모델 연결(product 모델 및 모든 필드를 사용하겠다.)
    class Meta:
        model = Product
        fields = '__all__'
