from django.contrib import admin
from django.urls import path, include

from users import user_urls
from posts import urls
from comments import comment_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include(user_urls)),
    path('post/', include(urls)),
    path("comment/", include(comment_urls))
]
