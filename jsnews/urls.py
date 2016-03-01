from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from articles.forms import LoginForm, RegisterForm
from django.views.generic.edit import CreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('articles.urls')),
    # https://docs.djangoproject.com/en/1.9/topics/auth/default/#all-authentication-views
    url(r'^login/$', auth_views.login, {'authentication_form': LoginForm}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),

    url(r'^register/$', CreateView.as_view(
        template_name='registration/register.html',
        form_class=RegisterForm,
        success_url='/'
    )),
]
