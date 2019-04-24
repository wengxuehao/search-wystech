from django.http import HttpResponse
from django.shortcuts import render
# import mysite.utils.restful
# Create your views here.
from django.views import View


# from mysite.utils.recognize import Character_View
# /home/wy/Desktop/search-wystech/mysite/utils/recognize.py
from .models import Recognize_model

class Recognize_Category_View(View):
    def get(self,request):
        categories = Recognize_model.objects.all()
        print(categories)
        # warn_sum = categories.count()
        return HttpResponse('ok')

class Character_recognition(View):
    def get(self, request):
        return render(request, 'search/char_search.html')

    def post(self, request):
        # 调用文字识别api
        # 返回识别结果供前端页面显示
        # self.char()
        # 前端提交图片到后台
        filepath = request.POST.get('filepath')
        data = self.char(filepath)
        return restful.result(data=data)

class Animal_recognition(View):
    def get(self, request):
        # 调用动物识别api
        # 返回识别结果供前端页面显示
        return render(request, 'search/animal_search.html')


class Plant_recognition(View):
    def get(self, request):
        # 调用植物识别api
        # 返回识别结果供前端页面显示
        return render(request, 'search/plant_search.html')
