from django import forms
from .models import Agendamento


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'contato', 'data', 'servico']
        widgets = {
            # mostra um calendário no campo de data
            'data': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
