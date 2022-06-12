from django.contrib import admin
from .models import Book, Another, Address, Country
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("another", "rating")
    list_display = ("title", "another")


admin.site.register(Book, BookAdmin)
admin.site.register(Another)
admin.site.register(Address)
admin.site.register(Country)