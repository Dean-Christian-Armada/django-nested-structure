"""test_people URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from login.views import index, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # START authentication URLS
    url(r'^$', index, name='home_page'),
    url(r'^logout/$', logout, name='log_out'),
    # END authentication URLS

    # START first level apps
    url(r'^app/', include('app.urls')),
    url(r'^testing-sample-app/', include('testing_sample_app.urls')),
    # END first level apps
]

# activating media urls
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)