from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class UserView(View):
    def get(self, request):
        #  跳转登录界面最好
        return HttpResponse('HELLO WORLD 这是登录页面')


class User_manage(View):
    def get(self, request):
        return HttpResponse('this is 用户管理界面')
