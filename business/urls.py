from django.conf.urls import url
from . import views

app_name = "business"


urlpatterns = [
    url('^$' , views.business , name = 'business'),
]
