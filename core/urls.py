from django.urls import path
from .views import *
urlpatterns = [
    path('book/', BookListCreateView.as_view() , name = 'books-list'),
    path('book/<int:pk>', BookDetailView.as_view(), name = 'book-detail')
]
