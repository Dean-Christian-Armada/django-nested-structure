from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='sub_app_1_index' ),
]