from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from CostosCirugia.models import *
from CostosCirugia.forms import *
from CostosCirugia.funciones.calculos import *

# Create your views here.
def index(request,*args, **kwargs):
    return render(request, 'index.html', {})

def login(request,*args, **kwargs):
    return render(request, 'login.html', {})


class consulta(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'CostosCirugia/consulta.html'
    success_url = reverse_lazy('consulta')


    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        #mandar resultados de la consulta
        consul = Consulta.objects.all()
        canas = Canasta.objects.all()
        honor_sal = HonorarioSalario.objects.all()
        proc = Procedimiento.objects.all()
        cons = Constante.objects.last()
        datos = calculo(1,2,consul,canas,honor_sal,proc,7,8,9,cons)#las entradas con numero significa que no son necesarios esos parametros para realizar los calulos requeridos
        datos.resultado()

        #mandar datos al template
        if datos.resultado():
            context['data'] = datos.resultado()
            context['data_graphic'] = [datos.resultado()[17],
                datos.resultado()[12][0][1],
                datos.resultado()[14],
                datos.resultado()[15],
                datos.resultado()[8],
                datos.resultado()[18],
                datos.resultado()[9],
            ]
        return context


class TipoProcedimientoCrear(CreateView):
    model = TipoProcedimiento
    form_class = TipoProcedimientoForm
    template_name = 'CostosCirugia/TipoProcedimiento_crear.html'
    success_url= reverse_lazy('TipoProcedimientoCrear')

    def post(self,request,*args,**kwargs):
        form = TipoProcedimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

class TipoProcedimientoList(ListView):
    model = TipoProcedimiento
    template_name = 'TipoProcedimientoList.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        especialidad = TipoProcedimiento.objects.all()
        context['TipoProcedimientos'] = especialidad
        return context