from django.contrib import admin

from . import models


class UnitInline(admin.TabularInline):
    model = models.Unit
    extra = 1


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user")
    list_display_links = ("id", "title")
    list_filter = ("user", "is_delete")
    search_fields = ("title",)
    date_hierarchy = "created_at"
    inlines = (UnitInline,)


class WordInline(admin.TabularInline):
    model = models.Word
    extra = 1


@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "book")
    list_display_links = ("id", "title")
    list_filter = ("book", "is_delete")
    search_fields = ("title",)
    date_hierarchy = "created_at"
    inlines = (WordInline,)


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "en", "ru", "uz", "unit")
    list_display_links = ("id", "en")
    list_filter = ("unit", "is_delete")
    search_fields = ("en", "ru", "uz")
    date_hierarchy = "created_at"
