from django.contrib import admin
from signupapp.models import details
# Register your models here.
class lAdmin(admin.ModelAdmin):
    list_display=['Name','Email','Password','ConfirmPassword']
admin.site.register(details,lAdmin)