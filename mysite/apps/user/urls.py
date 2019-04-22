from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.UserView.as_view(), name='login'),

    path('manage/',views.User_manage.as_view(),name='manage')
]