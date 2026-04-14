from django.urls import path
from .views import fetch_books, list_books, ask

urlpatterns = [
    path('fetch/', fetch_books),
    path('list/', list_books),
    path('ask/', ask),
]