#from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import ListView, DetailView
from .models import Pda

class PdaChangesListView(ListView):
    model = Pda
    template_name = ('japp_list.html')

class PdaChangesDetailView(DetailView):
    model = Pda
    template_name = ('japp_detail.html')


class PdaChangesRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'japp_register.html'
    success_url = reverse_lazy('japp_index')

class PdaChangesCreateView(CreateView):
    model = Pda
    template_name = 'japp_add.html'
    fields = ['text','cpu']
    success_url = reverse_lazy('japp_index')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PdaChangesCreateView, self).form_valid(form)
