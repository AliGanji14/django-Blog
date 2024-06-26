from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('create/', views.post_create_view, name='post_create'),
    path('<int:pk>/update/', views.post_update_view, name='post_update'),
    path('<int:pk>/delete/', views.post_delete_view, name='post_delete'),
]
