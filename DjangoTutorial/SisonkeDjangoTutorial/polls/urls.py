from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^jessy', views.something, name='Jessy'),
    url(r'^brian', views.something, name='Brian')
]
