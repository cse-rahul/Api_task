from django.contrib import admin
from .models import App

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_name', 'version', 'description')
