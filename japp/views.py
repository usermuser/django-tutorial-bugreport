#from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Pda

class PdaChangesListView(ListView):
    model = Pda
    template_name = ('japp_list.html')

class PdaChangesDetailView(DetailView):
    model = Pda
    template_name = ('japp_detail.html')
