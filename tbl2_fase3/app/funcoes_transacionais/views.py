from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from funcoes_transacionais.models import FuncaoTransacional

class FTransacionalList(ListView):
    model = FuncaoTransacional

class FTransacionalView(DetailView):
    model = FuncaoTransacional

class FTransacionalCreate(CreateView):
    model = FuncaoTransacional
    fields = ['nome', 'contador', 'tipo_funcao', 'complexidade', 'qtd_alr', 'qtd_der', 'pontos_de_funcao']
    success_url = reverse_lazy('ftrans_list')

class FTransacionalUpdate(UpdateView):
    model = FuncaoTransacional
    fields = ['nome', 'contador', 'tipo_funcao', 'complexidade', 'qtd_alr', 'qtd_der', 'pontos_de_funcao']
    success_url = reverse_lazy('ftrans_list')

class FTransacionalDelete(DeleteView):
    model = FuncaoTransacional
    success_url = reverse_lazy('ftrans_list')

