""" Newforms Admin configuration for Photologue

"""
from django.contrib import admin
from models import *


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'photo_count', 'is_public')
    list_filter = ['date_added', 'is_public']
    date_hierarchy = 'date_added'
    prepopulated_fields = {'title_slug': ('title',)}

    
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_taken', 'date_added', 'is_public', 'tags', 'view_count', 'admin_thumbnail')
    list_filter = ['date_added', 'is_public']
    list_per_page = 10
    prepopulated_fields = {'title_slug': ('title',)}

    
class PhotoEffectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'admin_sample')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Adjustments', {
            'fields': ('color', 'brightness', 'contrast', 'sharpness')
        }),
        ('Filters', {
            'fields': ('filters',)
        }),
        ('Reflection', {
            'fields': ('reflection_size', 'reflection_strength', 'background_color')
        }),
    )

    
class PhotoSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'height', 'crop', 'pre_cache', 'effect', 'increment_count')
    fieldsets = (
        (None, {
            'fields': ('name', 'width', 'height', 'quality')
        }),
        ('Options', {
            'fields': ('crop', 'pre_cache', 'increment_count')
        }),
        ('Enhancements', {
            'fields': ('effect', 'watermark',)
        }),
    )

    
class WatermarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'opacity', 'style')

    
pl_admin = admin.AdminSite()

pl_admin.register(Gallery, GalleryAdmin)
pl_admin.register(GalleryUpload)
pl_admin.register(Photo, PhotoAdmin)
pl_admin.register(PhotoEffect, PhotoEffectAdmin)
pl_admin.register(PhotoSize, PhotoSizeAdmin)
pl_admin.register(Watermark, WatermarkAdmin)






