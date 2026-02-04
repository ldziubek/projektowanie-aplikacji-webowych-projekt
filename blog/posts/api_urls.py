from django.urls import path, include
from . import api_views

urlpatterns = [
    path('topics/', api_views.topic_list),
    path('topics/<int:pk>/', api_views.topic_detail),
    path('topics/create/', api_views.topic_create),
    path('topics/search/<str:phrase>/', api_views.topic_search_by_name),
    path('topicscategories/search/<str:phrase>/', api_views.topic_and_category_search_by_name),
    path('categories/', api_views.category_list),
    path('categories/<int:pk>/', api_views.category_detail),
    path('categories/create/', api_views.category_create),
    path('categories/search/<str:phrase>/', api_views.category_search_by_name),
    path('posts/', api_views.post_list),
    path('posts/<int:pk>/', api_views.post_detail),
    path('posts/create/', api_views.post_create),
    path('posts/search/<str:phrase>/', api_views.post_search_by_name),
    path('user/posts/', api_views.user_post_list),
]