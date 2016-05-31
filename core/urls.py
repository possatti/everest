from django.conf.urls import url
from core import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.sitemap, name='index'),
    url(r'^skills/$', views.skills, name='skills'),
    url(r'^coding/$', views.coding, name='coding'),
    url(r'^signin/$', views.signin, name='signin'),
]
