from django.conf.urls import url
from . import views

app_name = "discover"


urlpatterns = [
    url('^$' , views.discover , name = 'discover'),
]
