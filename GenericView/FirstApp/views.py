from django.shortcuts import render
from .models import Laptop
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

# Create your views here.

class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/laptop/list/'

class LaptopListView(ListView):
    model = Laptop

class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/laptop/list/'

class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url = '/laptop/list/'

