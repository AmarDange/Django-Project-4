from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Me Marathi Administration"
admin.site.index_title = "Welcome to Me Marathi Admin Panel"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("blog.urls"), name="blog_urls"),
    # path("", include("comment.urls"), name="comment_urls"),
    path("accounts/", include("allauth.urls")),
]
