from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from funcoes_transacionais.models import FuncaoTransacional

class FTransacionalList(ListView):
    model = FuncaoTransacional
    
    def get_context_data(self, **kwargs):
        funcoes = super(FTransacionalList, self).get_context_data(**kwargs)
        funcoes['soma_ce'] = sum(i.pontos_de_funcao for i in FuncaoTransacional.objects.filter(tipo_funcao = 'CE')) 
        funcoes['soma_se'] = sum(i.pontos_de_funcao for i in FuncaoTransacional.objects.filter(tipo_funcao = 'SE'))
        funcoes['soma_ee'] =  sum(i.pontos_de_funcao for i in FuncaoTransacional.objects.filter(tipo_funcao = 'EE'))
        return funcoes

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

