from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='app_index' ),
	url(r'^sub-app-1/', include('app.subapp1.urls')),
	# url(r'^crew-onboard-list/', include('crew_menu.crew_onboard_list.urls')),
]