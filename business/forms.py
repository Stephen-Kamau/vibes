from django import forms
from .models import sell_goods

class sell_frm(forms.ModelForm):
    class Meta:
        model = sell_goods
        fields = ('itemdesc','price' , 'itemimg')

        widgets = {
            'itemdesc':forms.Textarea(attrs = {'rows':4 , 'cols':30 , 'name':'description'}),
        }
