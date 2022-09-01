from django.contrib import admin
from LinkField.models import BestSeller

# Register your models here.
from LinkField.models import Book,Author
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('author',)
    search_fields = ('author',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name_colored','book_link', 'author','author_link','is_available')
    autocomplete_fields = ('author','book')
    list_editable=("author",)
    search_fields=('name',)

    def name_colored(self,obj):
        if obj.is_available:
            color_code="00FF00"
        else:
            color_code="FF0000"
        html='<span style="color:#{};">{}</span>'.format(color_code,obj.name)
        return format_html(html)
    name_colored.short_description="name"

    def author_link(self,LinkField):
        url = reverse("admin:LinkField_author_change",args=[LinkField.author.id])
        link = '<a href="{}">{}</a>'.format(url, LinkField.author.author)
        return mark_safe(link)
    author_link.short_description = 'Change_AUTHOR'

    def book_link(self,LinkField):
        url=reverse("admin:LinkField_bestseller_change",args=[LinkField.book.id])
        link = '<a href="{}">{}</a>'.format(url,LinkField.book.book_name)
        return mark_safe(link)
    book_link.short_description= "Change_Book"

admin.site.register(Book,BookAdmin)

class BestSellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'rank', 'book_name')
    search_fields=('book_name',)
    
admin.site.register(BestSeller,BestSellerAdmin)
