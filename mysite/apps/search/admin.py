from django.contrib import admin

# Register your models here.
from .models import Recognize_model


class RecognizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


admin.site.register(Recognize_model, RecognizeAdmin)
