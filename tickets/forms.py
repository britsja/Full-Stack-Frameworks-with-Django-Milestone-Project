from django import forms
from .models import Comments, Ticket
from django.utils.translation import gettext_lazy as _

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment', 'created_date')
        labels = {
            'comment': _('Your Comment'),
            'created_date': _('Todays Date'),
        }

class TicketsForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = {'ticketname', 'description', 'category', 'created_date'}
        labels = {
            'ticketname': _ ('Ticket Title'),
            'description': _('Describe the problem'),
            'category': _('Support Category'),
            'created_date': _ ('Todays Date')
        }

