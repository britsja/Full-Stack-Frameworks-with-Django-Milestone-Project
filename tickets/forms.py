from django import forms
from .models import Comments
from django.utils.translation import gettext_lazy as _

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('ticket', 'commentusername', 'comment', 'created_date')
        labels = {
            'ticket': _('Ticket Title'),
            'commentusername': _('Username'),
            'comment': _('Your Comment'),
            'created_date': _('Todays Date'),
        }

      