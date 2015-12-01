from django import forms
from django.forms import ModelForm
from portal.models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ('id',)

















# titulo = forms.TextInput
# descripcion = forms.Textarea
# estado = forms.Select
# autor = forms.Select
