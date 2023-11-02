from django.urls import path
from .views import HomeView

app_name = "dictionary"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("<slug>/", ArticleDetailView.as_view(), name="article-detail"),
]
