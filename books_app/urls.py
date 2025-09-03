from django.urls import path
from .views import BookListCreate, BookDetail, FetchExternalData

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('fetch-external/', FetchExternalData.as_view(), name='fetch-external'),
]