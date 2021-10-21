from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe



class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    list_editable = ('cms_text', 'cms_css',)
    list_display_links = ('cms_title',)

    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.cms_img.url:
            return mark_safe(f'<img src = "{obj.cms_img.url}" width = "80px">')
        else:
            "Картинка не найдена"

    get_img.short_description = 'Миниатюра'

admin.site.register(CmsSlider, CmsAdmin)