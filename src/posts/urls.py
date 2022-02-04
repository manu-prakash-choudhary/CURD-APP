from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (
    load_post_data_view,
    post_list_and_create,
    like_unlike_post,
    post_detail
)
app_name = 'posts'
urlpatterns = [

    path('',post_list_and_create,name = 'main-board'),
    path('like-unlike/',like_unlike_post,name = 'like-unlike'),
    path('data/<int:num_posts>/',load_post_data_view,name='posts-data'),
    path('<pk>/',post_detail,name = 'post-detail'),
   
]

