from django.contrib import admin
from .models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'view')
    readonly_fields = ('view',)
    list_filter = ('created_at', 'updated_at')


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
