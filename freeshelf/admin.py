from django.contrib import admin
from freeshelf.models import Book
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'author', 'description', 'date', 'url')
    prepopulated_fields = {'slug': ('title',)}

admin.site.unregister(Book)
admin.site.register(Book, BookAdmin)