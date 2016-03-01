from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # https://docs.djangoproject.com/en/1.9/topics/auth/default/#using-the-views
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('articles.urls')),
    url(r'^admin/', admin.site.urls),
]
