from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class Index_view(View):
    def get(self,request):
        return render(request,'user/index.html')

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
        return render(request,'user/user_manage.html')
