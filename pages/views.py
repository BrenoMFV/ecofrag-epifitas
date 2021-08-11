from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from epifitas.models import Especie


class HomePageView(ListView):
    template_name = 'home.html'
    context_object_name = 'ultimas_adc_list'

    def get_queryset(self):
        return Especie.objects.all().order_by('-adicionada_em')[:5]


class AboutPageView(TemplateView):
    template_name = 'about.html'
