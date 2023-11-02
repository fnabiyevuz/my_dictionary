from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from .models import Book, Unit, Word


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        books = Book.objects.filter(user=self.request.user)

        context['home'] = 'active'
        context['books'] = books

        return context
