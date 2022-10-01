from django.contrib import admin
from django.urls import path
from books.views import books_view, books_pub_date


urlpatterns = [
    path('books/', books_view, name='books'),
    path('admin/', admin.site.urls),
    path('books/<pub_date>/', books_pub_date, name='book'),
]