from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.modelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']