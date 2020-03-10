from django.contrib import admin
from .models import groups,members
# Register your models here.

class viewer(admin.ModelAdmin):
    model = members
    list_display = ("memberuid" ,)

admin.site.register(members , viewer)

class viewer(admin.ModelAdmin):
    model = groups
    list_display = ("gid","group_name" , "location" , "gicon")


admin.site.register(groups , viewer)
