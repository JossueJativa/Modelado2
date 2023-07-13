from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pagCentroCostos', views.pagCentroCostos, name='pagCentroCostos'),
    path('centrocostos', views.centrocostos, name='centrocostos'),
    path('pagTipoTrabajador', views.pagTipoTrabajador, name='pagTipoTrabajador'),
    path('pagTipoContrato', views.pagTipoContrato, name='pagTipoContrato'),
    path('pagNivelSalarial', views.pagNivelSalarial, name='pagNivelSalarial'),
    path('pagCategoriaOcupacional', views.pagCategoriaOcupacional, name='pagCategoriaOcupacional'),
    path('pagTipoCese', views.pagTipoCese, name='pagTipoCese'),
    path('pagEstadoTrabajador', views.pagEstadoTrabajador, name='pagEstadoTrabajador'),
    path('pagTipoTrabajador', views.pagTipoTrabajador, name='pagTipoTrabajador'),
    path('agregarCentroCostos', views.agregarCentroCostos, name='agregarCentroCostos'),
    path('eliminarCentroCostos/<str:id>/<str:descripcion>', views.eliminarCentroCostos, name='eliminarCentroCostos'),
    path('editCentroCostos/<str:id>', views.editCentroCostos, name='editCentroCostos'),
    path('edit/<str:id>', views.edit, name='edit'),

    ##Movimiento de plantilla
    path('PagMovimientoPlanilla', views.PagMovimientoPlanilla, name='PagMovimientoPlanilla'),
    path('PagMovimientoPlanillaSearch', views.PagMovimientoPlanillaSearch, name='PagMovimientoPlanillaSearch'),
    path('PagMovimientoPlanillaEdit/<str:id>', views.PagMovimientoPlanillaEdit, name='PagMovimientoPlanillaEdit'),
    path('editMovimientoPlantilla/<str:id>', views.editMovimientoPlantilla, name='editMovimientoPlantilla'),
    path('PagMovimientoPlanillaCreate', views.PagMovimientoPlanillaCreate, name='PagMovimientoPlanillaCreate'),
    path('pushMovimientoPlantilla', views.pushMovimientoPlantilla, name='pushMovimientoPlantilla'),
    path('eliminarMovimientoPlanilla/<str:id>', views.eliminarMovimientoPlanilla, name='eliminarMovimientoPlanilla'),

    ##Trabajador
]