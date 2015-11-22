# -*- coding: utf8 -*-

from django import forms
from prospectos.models import Prospecto

class ProspectoForm(forms.ModelForm):

    genero = forms.ChoiceField(
        label=u'Género',
        widget=forms.RadioSelect,
        choices=Prospecto.OPCIONES_GENERO
    )

    class Meta:
        model = Prospecto
        exclude = ('id', 'created', 'modified')
