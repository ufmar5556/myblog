from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("posts/", views.post_list, name="post_list"),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),  # New detail page URL
    path("create/", views.create_post, name="create_post")
]
