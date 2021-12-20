from django import forms
from trackApp.models import Nemareturnform

# class TrackappDocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'document', )
#         docfile = forms.FileField(label='Select a file')

class NemareturnformForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
