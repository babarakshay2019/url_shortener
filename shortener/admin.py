from django.contrib import admin

from .models import URLMapping

class URLMappingAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'visit_count', 'long_url')
    search_fields = ('short_code', 'long_url')

admin.site.register(URLMapping, URLMappingAdmin)
