from django import forms
from django.forms import Textarea
from .models import Comments, Ticket
from django.utils.translation import gettext_lazy as _

# Views to create comment forms and ticket forms

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'comment'}
        labels = {
            'comment': _('Your Comment'),
        }

class TicketsForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = {'ticketname', 'description', 'category'}
        labels = {
            'ticketname': _ ('Ticket Title'),
            'description': _('Describe the problem'),
            'category': _('Support Category'),
        }

        widgets = {
            'description': Textarea(attrs={'rows': 10}),
        }

        order_fields = ('category', 'ticketname', 'description')

