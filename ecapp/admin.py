from django.contrib import admin
from ecapp.models import course
# Register your models here.
class CAdmin(admin.ModelAdmin):
    list_display=['Coursename']
admin.site.register(course,CAdmin)