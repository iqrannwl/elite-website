from django.urls import path
from blogs.views import blog_list, blog_detail


urlpatterns=[
    path("", blog_list, name="blogs"),
    path("<int:id>", blog_detail, name="blog_detail")
]