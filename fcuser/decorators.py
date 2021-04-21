from django.shortcuts import redirect
from .models import Fcuser

# wrapping 함수와 기존 함수의 인자값을 맞춰줘야 함.
def login_required(function):
    def wrap(request, *args, **kwargs):
        # 로그인 확인해서 로그인이 없는 경우 login 화면으로 이동시켜줌
        # 따라서 decorator 표시만 하면 앞으로는 따로 구현할 필요없이 login 화면으로 넘어간다.
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        # 로그인 확인해서 로그인이 없는 경우 login 화면으로 이동시켜줌
        # 따라서 decorator 표시만 하면 앞으로는 따로 구현할 필요없이 login 화면으로 넘어간다.
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        #user의 level이 admin인지 확인(여기서 admin은 장고의 admin이 아닌 제품을 등록하는 관리자를 의미)
        user = Fcuser.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')
        return function(request, *args, **kwargs)

    return wrap