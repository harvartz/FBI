from django.contrib import admin
from fbiapp.models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name']
    search_filds = ['user_id']
