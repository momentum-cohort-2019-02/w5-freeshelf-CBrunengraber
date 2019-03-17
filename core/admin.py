from django.contrib import admin
from core.models import Author, Book

admin.site.register(Book)
admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('slug')