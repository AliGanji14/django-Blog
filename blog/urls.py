from django.urls import path

from . import views
urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('create/', views.post_new_view, name='post_create'),
]
