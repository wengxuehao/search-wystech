from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('char/', views.Character_recognition.as_view(), name='char'),  # 通用文字识别
    path('animal/', views.Animal_recognition.as_view(), name='annimal'),  # 动物识别
    path('plant/', views.Plant_recognition.as_view(), name='plant')  # 植物识别
]
