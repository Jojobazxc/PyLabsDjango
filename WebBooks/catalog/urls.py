from django.contrib import admin
from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('', index, name="index"),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path(r'^authors/$', views.AuthorListView.as_view(), name='authors')
]
