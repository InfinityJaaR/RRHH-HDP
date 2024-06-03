# urls.py en tu aplicación
from django.urls import path
from .views import *

urlpatterns = [
   
    path('empleado/perfil/<id>', GestionarEmpleadosView, name="perfil_empleado"),
    path('empleado/permisos/<id>',GestionarPermisosView, name='gestionar_permisosEM'),
    path('administrador/organizacion/cargos', AdministrarCargoView, name="AdministrarCargoView"),
    path('administrador/pagos/nuevoPago',CrearPagoView, name="CrearPagoView"),
    path('empleado/permisos/solicitarPermiso/<id>',SolicitarPermisoView, name='solicitar_permiso'),
    path('',HomeView, name= "HomeView"),
    #ruta pantallas Eduardo
    path('administrador/Organizacion/areas',AdministrarAreaView, name="AdministrarAreaView"),
    path('administrador/Organizacion/areas/gestionarArea',GestionarAreaView),
    path('administrador/Organizacion/cargos/gestionarCargo',GestionarCargoView, name="GestionarCargoView"),
    path('administrador/permisos',GestionarPermisoADView),
    path('administrador/Organizacion',GestionarOrganizacionView,name="GestionarOrganizacionView"),
    path('administrador/pagos/modificar',ModificarPagoView, name="ModificarPagoView"),
    #Crear empleado
    path('administrador/empleado',GestionarEmpleadoADView, name='GestionarEmpleadoADView'),
    path('get_cargos/', get_cargos, name='get_cargos'),
    path('get_municipios/', get_municipios, name='get_municipios'),

    
    path('administrador/pagos',GestionarPagoADView),
    path('empleado/pagos/<id>',GestionarPagoEMView, name='mis_pagos'),
    path('EliminarCargo/<int:id>', EliminarCargo, name="EliminarCargo"),
    path('EliminarArea/<int:id>', EliminarArea, name="EliminarArea"),
    path('EliminarEmpleadp/<id>', EliminarEmpleado, name="EliminarEmpleado"),
    path('ModificarCargo/<id>', ModificarCargo, name="ModificarCargo"),
    path('ModificarArea/<id>', ModificarArea, name="ModificarArea"),
    path('registro/<id>',Registro,name="Registro"),
    path('logout/',exit,name="exit" ),
    
    path('administrador/asistencia',RegistrarAsistenciaView),
    # path('administrador/asistencias',RegistrarAsistenciaView, name="RegistrarAsistenciaView"),
    # path('administrador/asistencias/guardar', save_csv, name="save_csv"),
]
