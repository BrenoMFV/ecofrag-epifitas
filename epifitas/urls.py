from django.urls import path

from .views import EpifitasListView, EpifitaDetailView

urlpatterns = [
    path('list-all/', EpifitasListView.as_view(), name='epifitas_list'),
    path('<uuid:pk>/', EpifitaDetailView.as_view(), name='epifita_detail'),
]