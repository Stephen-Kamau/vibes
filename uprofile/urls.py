from django.conf.urls import url
from . import views

app_name = "profile"


urlpatterns = [
    url('^$' , views.profile , name = 'profile'),
]
