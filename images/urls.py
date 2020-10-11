from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# app_name = 'images'

urlpatterns=[
    #post views
    path('',views.image,name='image'),
    path('search/',views.search_results,name='search_results'),
    path('detail/(\d+)',views.detail,name='detail'),
    path('location/(\d+)',views.location,name='location'),

]

if settings.DEBUG: 
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)