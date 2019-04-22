from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class Character_recognition(View):
    def get(self, request):
        # 调用文字识别
        return HttpResponse('this is 文字识别')


class Animal_recognition(View):
    def get(self, request):
        return HttpResponse('this is 动物识别')


class Plant_recognition(View):
    def get(self, request):
        return HttpResponse('this is 植物识别')
