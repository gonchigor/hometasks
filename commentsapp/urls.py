from django.urls import path
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView

app_name = 'comments'
urlpatterns = [
    path('create/', CommentCreateView.as_view, name='create'),
    path('<int:pk>/update/', CommentUpdateView.as_view, name='update'),
    path('<int:pk>/delete/', CommentDeleteView.as_view, name='delete'),
]
