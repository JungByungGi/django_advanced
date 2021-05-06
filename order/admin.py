from django.contrib import admin
from .models import Order
from django.utils.html import format_html   # html escape를 안 통하게 함(html처럼 태그로 쓰겠다.)


# 관리자 페이지 커스터마이징
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)  # 필터 항목 활성화
    list_display = ('fcuser', 'product', 'styled_status')

    # 상태 필터 커스터마이징
    # f는 문자열 formatting
    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        if obj.status == '결제완료':
            return format_html(f'<span style="color:blue">{obj.status}</span>')

        return obj.status
    
    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': '주문 목록'}
        return super().changelist_view(request, extra_context)
    
    # 상태바 변경
    styled_status.short_description = '상태'


admin.site.register(Order, OrderAdmin)
