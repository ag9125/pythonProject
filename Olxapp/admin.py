from django.contrib import admin
from Olxapp.models import Olx,Category,Image
class Olx_item(admin.ModelAdmin):
    list_ = ('recipe_name','recipe_des','recipe_image')
admin.site.register(Olx,Olx_item)
admin.site.register(Category)
admin.site.register(Image)


# Register your models here.


# Register your models here.


