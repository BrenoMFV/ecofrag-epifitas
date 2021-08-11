from django.urls import path
from django.views.generic import TemplateView, ListView, DetailView

from .models import Especie


class EpifitasListView(ListView):
    model = Especie
    template_name = 'epifitas/epifitas_list.html'
    paginate_by = 15
    # ordering = Especie.sinonimia



class EpifitaDetailView(DetailView):
    model = Especie
    template_name = 'epifitas/epifita_detail.html'


