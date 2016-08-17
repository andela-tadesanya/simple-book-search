from django.contrib import admin
from .models import Category, Book


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


class BookAdmin(admin.ModelAdmin):
    fields = ('name', 'ISBN', 'category')
    list_display = ('name', 'ISBN', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
