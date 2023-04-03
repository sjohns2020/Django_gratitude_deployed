from django import forms

from .models import Org

class OrgForm(forms.ModelForm):

    class Meta:
        model = Org
        fields = ('name', 'website', 'date_added', 'stars', 'upload' )
