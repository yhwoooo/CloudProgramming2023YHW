from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('category/<str:slug>/', views.categories_page),
    path('tag/<str:slug>/', views.tag_page),
    # path('<int:post_num>/', views.single_post_page),
]