from django.conf.urls import url
from . import views

app_name = "groups"


urlpatterns = [
    url('^$' , views.groups , name = 'groups'),
]
