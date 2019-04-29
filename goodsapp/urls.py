from django.urls import path
from goodsapp.views import BookDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    ]
