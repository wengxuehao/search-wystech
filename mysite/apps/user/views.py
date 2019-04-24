from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import User


class Index_view(View):
    def get(self, request):
        return render(request, 'user/index.html')


class UserView(View):
    def get(self, request):
        #  跳转登录界面最好
        # return HttpResponse('HELLO WORLD 这是登录页面')
        return render(request, 'user/login.html')


class User_manage(View):
    '''
    用户管理页面
    支持用户更换头像
    用户修改密码
    '''

    def get(self, request):
        return render(request, 'user/user_manage.html')

    def post(self, request):
        '''
        用户修改个人信息
        修改手机号码和用户名
        '''
        name = request.POST.get('name','')
        telephone = request.POST.get('telephone','')
        user = User.objects.filter(id=id)
        user.telephone = telephone
        user.name=name
        user.save()
        return HttpResponse('ok')
