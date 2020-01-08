from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('books',views.BooklistView.as_view(),name = 'books'),
    path('authors',views.AuthorlistView.as_view(),name = 'authors'),
    path('authors/<int:pk>',views.AuthorDetailView.as_view(),name = 'author-details'),
    path('books/<int:pk>',views.BookDetailView.as_view(),name='book-details')
]