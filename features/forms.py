from django import forms
from django.forms import Textarea
from .models import Features, FeatureComments
from django.utils.translation import gettext_lazy as _

# Generate forms to add comments and add features

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
            'featurename': _ ('Feature Title or Name'),
            'description': _('Describe the required feature'),
        }
        
        order_fields = ('featurename', 'description')

        widgets = {
            'description': Textarea(attrs={'rows': 10}),
        }