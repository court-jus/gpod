from django.contrib import admin
from .models import POD, Picture


class PODAdmin(admin.ModelAdmin):
    pass


admin.site.register(POD, PODAdmin)


class PictureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Picture, PictureAdmin)
