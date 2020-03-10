from django.conf.urls import url
from . import views

app_name = "groups"


urlpatterns = [
url('^$' , views.groups , name = 'groups'),
url("^creategroup/" , views.creategroup , name = "creategroup"),
url("^creategroup(?P<gid>[\d]*)/" , views.join_group , name = "join_group")
]
