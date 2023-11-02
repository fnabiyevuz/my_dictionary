from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user")
    list_display_links = ("id", "title")
    list_filter = ("user", "is_delete")
    search_fields = ("title",)
    date_hierarchy = "created_at"


@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "book")
    list_display_links = ("id", "title")
    list_filter = ("book", "is_delete")
    search_fields = ("title",)
    date_hierarchy = "created_at"


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "en", "ru", "uz", "unit")
    list_display_links = ("id", "en")
    list_filter = ("unit", "is_delete")
    search_fields = ("en", "ru", "uz")
    date_hierarchy = "created_at"
