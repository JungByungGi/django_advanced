from django.contrib import admin
from .models import Fcuser


# Register your models here.
# changelist_view, changeform_view는 각 해당 페이지에 접속했을 때 ModelAdmin에서 호출되는데 함수 선언을 통해 중간에 함수를 끼워놓고 그 후에 원래 함수 호출.
class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

    # 장고 관리자 페이지의 사용자 페이지에 들어갔을 때 함수 호출됨.
    def changelist_view(self, request, extra_context=None):
        # 우리가 원하는 동작을 하고 원래 ModelAdmin에 만들어져 있는 changelist_view함수를 호출해라
        extra_context = { 'title': '사용자 목록'}
        return super().changelist_view(request, extra_context)

    # 장고 관리자 페이지의 사용자 상세보기 페이지에 들어갔을 때 함수 호출됨.
    # 상세보기 페이지의 경우 각 목록에서 해당하는 id를 클릭하여 상세보기로 넘어가고 수정 후 어느 주소로 보내야 할 지에 대한 정보가 있어야 하므로 인자값이 다음과 같다.
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        fcuser = Fcuser.objects.get(pk=object_id)
        extra_context = {'title': f'{fcuser.email} 수정하기'}
        return super().changeform_view(request, object_id, form_url, extra_context)

admin.site.register(Fcuser, FcuserAdmin)
