from django import forms
from .models import AboutModel
from ckeditor.widgets import CKEditorWidget
from utils import utils


class AboutModelForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutModel
        fields = ['title', 'description', 'video_url']
    def clean(self):
        return utils.allowed_one(AboutModel, self.instance.pk)
