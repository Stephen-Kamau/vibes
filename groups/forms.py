from django.forms import *
from .models import groups


class gform(ModelForm):
    class Meta:
        model = groups
        fields = ("group_name" , "gicon")
