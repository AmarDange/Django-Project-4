from . import views
from blog import views
from django.urls import path, include

urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    # path('', views.index, name='memarathi'),
    path("post_detail/<slug:slug>/", views.PostDetail, name="post_detail"),
    path("", views.AllDestination.as_view(), name="home"),
    path("about", views.about, name="about"),
    path("food", views.food, name="food"),
    path("blog", views.AllBlogPost.as_view(), name="all-blog"),
    path("user_page", views.User.as_view(), name="user-page"),
    path("add_post", views.AddPost.as_view(), name="add-post"),
    path("search", views.search, name="search"),
    path(
        "destinations_post/<str:des>",
        views.destinations_view,
        name="destinations-post",
    ),
    path(
        "user_post_list/", views.UserPostList.as_view(), name="user-post-list"
    ),
    path("like/<slug:slug>/", views.PostLike.as_view(), name="post_like"),
    path("update_post/<slug:slug>/", views.update_post, name="update-post"),
    path(
        "delete_post/<slug:slug>/",
        views.DeletePost.as_view(),
        name="delete-post",
    ),

        path("add_comment/<int:post_id>", views.add_comment, name="add_comment"),
    path(
        "edit_comment/<int:pk>",
        views.EditComment.as_view(),
        name="edit_comment",
    ),
    path(
        "delete_comment/<int:comment_id>",
        views.delete_comment,
        name="delete_comment",
    ),
]
