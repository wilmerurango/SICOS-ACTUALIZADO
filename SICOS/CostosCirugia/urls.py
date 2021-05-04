from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index,name="index"),
    path('login', login,name="login"),
    path('consulta', consulta.as_view(),name="consulta"),

    path('TipoProcedimientoCrear', TipoProcedimientoCrear.as_view(),name="TipoProcedimientoCrear"),
    path('TipoProcedimientoList', TipoProcedimientoList.as_view(),name="TipoProcedimientoList"),
    path('TipoProcedimientoEdit/<int:pk>/', TipoProcedimientoEdit.as_view(),name="TipoProcedimientoEdit"),

    path('NombreCanastaCrear', NombreCanastaCrear.as_view(),name="NombreCanastaCrear"),
    path('NombreCanastaList', NombreCanastaList.as_view(),name="NombreCanastaList"),
    path('NombreCanastaEdit/<int:pk>/', NombreCanastaEdit.as_view(),name="NombreCanastaEdit"),

    path('ConceptoHonorarioSalarioCrear', ConceptoHonorarioSalarioCrear.as_view(),name="ConceptoHonorarioSalarioCrear"),
    path('ConceptoHonorarioSalarioList', ConceptoHonorarioSalarioList.as_view(),name="ConceptoHonorarioSalarioList"),
    path('ConceptoHonorarioSalarioEdit/<int:pk>/', ConceptoHonorarioSalarioEdit.as_view(),name="ConceptoHonorarioSalarioEdit"),

    path('ActividadCrear', ActividadCrear.as_view(),name="ActividadCrear"),
    path('ActividadList', ActividadList.as_view(),name="ActividadList"),
    path('ActividadEdit/<int:pk>/', ActividadEdit.as_view(),name="ActividadEdit"),

    path('ConstanteCrear', ConstanteCrear.as_view(),name="ConstanteCrear"),
    path('ConstanteList', ConstanteList.as_view(),name="ConstanteList"),
    path('ConstanteEdit/<int:pk>/', ConstanteEdit.as_view(),name="ConstanteEdit"),
]
