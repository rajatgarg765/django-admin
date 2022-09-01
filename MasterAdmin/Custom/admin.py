from django.contrib import admin
from Custom.models import Book, Category, BestSellerBook
# Register your models here.
from django.utils.html import format_html
from django.contrib.postgres import fields

from django_json_widget.widgets import JSONEditorWidget
class BookAdmin(admin.ModelAdmin):
    list_display=('id','name_colored','author','published_date','is_available')
    list_filter=('is_available',)
    list_per_page=10
    search_fields=('name',)
    date_hierarchy='published_date'
    readonly_fields = ('created_at', 'updated_at')
    list_editable=('author',)

    def name_colored(self,obj):
        if obj.is_available:
            color_code="00FF00"
        else:
            color_code="FF0000"
        html='<span style="color:#{};">{}</span>'.format(color_code,obj.name)
        return format_html(html)

    name_colored.admin_order_field='name'
    name_colored.short_description='name'

admin.site.register(Book,BookAdmin)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('book_category',)

class BestSellerAdmin(admin.ModelAdmin):
    list_display=('id','rank','year')
    search_fields=('rank',)

admin.site.register(BestSellerBook, BestSellerAdmin)