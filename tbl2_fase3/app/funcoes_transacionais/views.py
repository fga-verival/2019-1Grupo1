from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from funcoes_transacionais.models import FuncaoTransacional

class FTransacionalList(ListView):
    model = FuncaoTransacional
    
    def get_context_data(self, **kwargs):
        
        query_ft_ce = FuncaoTransacional.objects.filter(tipo_funcao = 'CE')
        query_ft_se = FuncaoTransacional.objects.filter(tipo_funcao = 'SE')
        query_ft_ee = FuncaoTransacional.objects.filter(tipo_funcao = 'EE')

        funcoes = super(FTransacionalList, self).get_context_data(**kwargs)

        funcoes['soma_ce'] = self.get_sum(query_ft_ce)
        funcoes['soma_ee'] = self.get_sum(query_ft_ee)
        funcoes['soma_se'] = self.get_sum(query_ft_se)

        return funcoes

    def get_sum(self, query):

        pf_values = list(map(lambda obj : obj.pontos_de_funcao, query))
    
        return sum(pf_values)


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

