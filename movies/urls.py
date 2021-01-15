from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^youtube/(\d+)',views.youtube, name='youtube'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
