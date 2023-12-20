from django import forms
from reserva.models import Reserva

class ResevaForm(forms.ModelForm):
    model = Reserva
    fields = [
        'nomes', 'email', 'nome_pet', 'data', 'turno', 'tamanho', 'observacoes'
    ]