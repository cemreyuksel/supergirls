from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add', views.add, name='add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^impressum', views.impressum, name='impressum')
]
