from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'telephone', 'password','icon','email']


admin.site.register(User, UserAdmin)
