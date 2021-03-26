from django.contrib import admin
from django.urls import path, include

from CostosCirugia.views import *

urlpatterns = [
    path('', index,name="index"),
    path('login', login,name="login"),
    # path('consulta_plantilla', consulta_plantilla,name="consulta_plantilla"),
    path('consulta', consulta.as_view(),name="consulta"),
]
