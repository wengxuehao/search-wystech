from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('char/', views.Character_recognition.as_view(), name='char'),
    path('animal/',views.Animal_recognition.as_view(),name='annimal'),
    path('plant/',views.Plant_recognition.as_view(),name='plant')
]