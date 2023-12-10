from django.urls import path
from homepage.views import PostList, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
]