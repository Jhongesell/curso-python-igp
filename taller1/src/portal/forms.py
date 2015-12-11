from django import forms
from portal.models import Ticket
from portal.models import Producto


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ()

PRODUCTOS = (
    # ('0', '-------------------'),
    ('1', 'Samsung Galaxy S6'),
    ('2', 'TV LG 32" '),
    ('3', 'iPad 4'),
)

class VentaForm(forms.Form):
    cantidad = forms.IntegerField()
    producto = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=Producto.objects.all(),
        initial=2)
    cliente = forms.CharField(max_length=30)

    # producto2 = forms.ChoiceField(widget=forms.Select, choices=PRODUCTOS, initial= 3)




