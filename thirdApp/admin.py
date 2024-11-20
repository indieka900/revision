from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Team, CustomUser

admin.site.register(Team)
admin.site.register(CustomUser)
