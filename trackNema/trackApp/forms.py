from django import forms
from trackApp.models import Document, TrackappDocument

class TrackappDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
