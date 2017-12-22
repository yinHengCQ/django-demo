from django.contrib import admin
from models import *

# Register your models here.
class BoolInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','content','gender','book']

admin.site.register(BoolInfo,BoolInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)