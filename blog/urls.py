from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('new/', views.PostCreateView.as_view(), name='post_create'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<str:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('<str:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
