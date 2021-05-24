from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.conf.settings import AUTH_USER_MODEL
# Register your models here.


admin.site.register(User,BaseUserAdmin)
admin.site.register(Post)
