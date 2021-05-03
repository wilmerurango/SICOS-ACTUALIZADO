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
]
