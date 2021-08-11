from django.urls import path

from .views import EpifitasListView, EpifitaDetailView, GenericSearchResultsView

urlpatterns = [
    path('list-all/', EpifitasListView.as_view(), name='epifitas_list'),
    path('<uuid:pk>/', EpifitaDetailView.as_view(), name='epifita_detail'),
    path('search/', GenericSearchResultsView.as_view(), name='generic_search_results'),
]