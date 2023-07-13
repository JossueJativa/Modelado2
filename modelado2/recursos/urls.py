from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('centrocostos', views.centrocostos, name='centrocostos'),
    path('pagTipoTrabajador', views.pagTipoTrabajador, name='pagTipoTrabajador'),
    path('pagTipoContrato', views.pagTipoContrato, name='pagTipoContrato'),
    path('pagNivelSalarial', views.pagNivelSalarial, name='pagNivelSalarial'),
    path('pagCategoriaOcupacional', views.pagCategoriaOcupacional, name='pagCategoriaOcupacional'),
    path('pagTipoCese', views.pagTipoCese, name='pagTipoCese'),
    path('pagEstadoTrabajador', views.pagEstadoTrabajador, name='pagEstadoTrabajador'),
    path('pagTipoTrabajador', views.pagTipoTrabajador, name='pagTipoTrabajador'),
]