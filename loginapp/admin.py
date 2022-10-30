from django.contrib import admin
from loginapp.models import login
# Register your models here.
class lAdmin(admin.ModelAdmin):
    list_display=['username','password']
admin.site.register(login,lAdmin)