from django.conf.urls import url
from . import views

app_name = "discover"


urlpatterns = [
url("^followBot/(?P<fid>[\d]*)/"  , views.followBot , name = "followBot"),
    url('^$' , views.discover , name = 'discover'),
]
