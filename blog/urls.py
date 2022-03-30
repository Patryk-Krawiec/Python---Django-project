from django.urls import path
from .views import (PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
    UserPostListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-start'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/nowy/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/usun/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-onas'),
]
