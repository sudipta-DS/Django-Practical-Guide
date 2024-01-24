from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug":("title",),
    }
    list_display = ("title","rating","author","slug")
    list_filter = ("rating",)

admin.site.register(Book,BookAdmin)