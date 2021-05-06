from django.contrib import admin
from .models import Fcuser


# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

    # 장고 관리자 페이지의 사용자 페이지에 들어갔을 때 함수 호출됨.
    def changelist_view(self, request, extra_context=None):

        # 우리가 원하는 동작을 하고 원래 ModelAdmin에 만들어져 있는 changelist_view함수를 호출해라
        extra_context = { 'title': '사용자 목록'}
        return super().changelist_view(request, extra_context)

admin.site.register(Fcuser, FcuserAdmin)
