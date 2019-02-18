from django import forms
from django.forms import Textarea
from .models import Features, FeatureComments
from django.utils.translation import gettext_lazy as _

class CommentsForm(forms.ModelForm):
    class Meta:
        model = FeatureComments
        fields = {'comment'}
        labels = {
            'comment': _('Your Comment'),
        }

class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = {'featurename', 'description'}
        labels = {
            'featurename': _ ('Feature Title'),
            'description': _('Describe the problem'),
        }
        
        order_fields = ('featurename', 'description')

        widgets = {
            'description': Textarea(attrs={'rows': 10}),
        }