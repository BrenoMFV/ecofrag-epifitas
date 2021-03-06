from django.urls import path
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from .models import Especie


class EpifitasListView(ListView):
    model = Especie
    template_name = 'epifitas/epifitas_list.html'
    paginate_by = 30
    # ordering = Especie.sinonimia


class EpifitaDetailView(DetailView):
    model = Especie
    template_name = 'epifitas/epifita_detail.html'


class GenericSearchResultsView(ListView):
    model = Especie
    context_object_name = 'especies_results_list'
    template_name = 'epifitas/generic_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Especie.objects.filter(
            Q(sinonimia__icontains=query) |
            Q(genero__icontains=query) |
            Q(inforeproducao__flor__icontains=query) |
            Q(inforeproducao__fruto__icontains=query) |
            Q(inforeproducao__antese__icontains=query) |
            Q(inforeproducao__tipo_reproducao__icontains=query) |
            Q(inforeproducao__semente__icontains=query) |
            Q(inforeproducao__recursos_oferecidos__icontains=query)
        ).distinct().prefetch_related()
