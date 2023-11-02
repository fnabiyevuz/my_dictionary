from django.db import models

from apps.common.models import BaseModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Book(BaseModel):
    title = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_book')
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
        ordering = ("-created_at",)
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Unit(BaseModel):
    title = models.CharField(max_length=60)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='book_unit')
    order = models.PositiveSmallIntegerField(default=1)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "unit"
        ordering = ("order",)
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'


class Word(BaseModel):
    en = models.CharField(max_length=255, null=True, blank=True)
    ru = models.CharField(max_length=255, null=True, blank=True)
    uz = models.CharField(max_length=255, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, related_name='unit_word')
    description = RichTextField(null=True, blank=True)
    is_memorize = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.en

    class Meta:
        db_table = "word"
        ordering = ("en",)
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
