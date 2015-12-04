from django import forms
from portal.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ('id',)

