from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm


# R - READ: lista todos os agendamentos
def lista(request):
    agendamentos = Agendamento.objects.order_by('data')
    return render(request, 'agendamentos/lista.html', {'agendamentos': agendamentos})


# R - READ: mostra um agendamento
def detalhe(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    return render(request, 'agendamentos/detalhe.html', {'agendamento': agendamento})


# C - CREATE: cadastra um novo agendamento
def criar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamentos:lista')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamentos/form.html', {'form': form, 'titulo': 'Novo agendamento'})


# U - UPDATE: edita um agendamento existente
def editar(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('agendamentos:detalhe', id)
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'agendamentos/form.html', {'form': form, 'titulo': 'Editar agendamento'})


# D - DELETE: exclui um agendamento (somente via POST)
def excluir(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('agendamentos:lista')
    return redirect('agendamentos:detalhe', id)
