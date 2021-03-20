from django.shortcuts import render
from CostosCirugia.models import *

# Create your views here.
def index(request,*args, **kwargs):
    return render(request, 'index.html', {})

def login(request,*args, **kwargs):
    return render(request, 'login.html', {})

def consulta(request,*args, **kwargs):
    objeto = Canasta.objects.all()
    contexto = {'canastas':objeto}
    return render(request, 'CostosCirugia/consulta.html', contexto)