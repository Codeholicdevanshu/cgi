from django.contrib import admin
from .models import UserDetails
# Register your models here.

@admin.register(UserDetails)
class AdminUserDetails(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','email','password']

