from django.contrib import admin
from .models import *
# Register your models here.


class ClassImageInline(admin.TabularInline):
    model = ClassImage
    extra = 1


class ImgAdmin(admin.ModelAdmin):
    inlines = [ClassImageInline]


admin.site.register(Img, ImgAdmin)
admin.site.register(ContactRequest)



