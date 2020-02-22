from django.conf.urls import url
from . import views

app_name = "messaging"


urlpatterns = [
    url('^$' , views.messaging , name = 'messaging'),
]
