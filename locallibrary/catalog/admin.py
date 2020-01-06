from django.contrib import admin
from .models import Genre,Book,BookInstance,Author
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')

@admin.register (BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status')

admin.site.register(Genre)
admin.site.register(Author)

