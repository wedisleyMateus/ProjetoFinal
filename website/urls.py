from django.urls import include, path, re_path 
from .views import home 


urlpatterns = [
    path(r'', home, name='website_home'),
]
