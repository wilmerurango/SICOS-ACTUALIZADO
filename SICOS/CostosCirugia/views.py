from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import *
from .funciones.calculos import *

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

    # def get_context_data(self,*args,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     especialidad = TipoProcedimiento.objects.all()
    #     context['TipoProcedimientos'] = especialidad
    #     return context

class TipoProcedimientoEdit(UpdateView):
    model = TipoProcedimiento
    form_class = TipoProcedimientoForm
    template_name = 'CostosCirugia/TipoProcedimiento_edit.html'
    success_url= reverse_lazy('TipoProcedimientoList')



class NombreCanastaCrear(CreateView):
    model = NombreCanasta
    form_class = NombreCanastaForm
    template_name = 'CostosCirugia/NombreCanasta_crear.html'
    success_url= reverse_lazy('NombreCanastaCrear')

    def post(self,request,*args,**kwargs):
        form = NombreCanastaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

class NombreCanastaList(ListView):
    model = NombreCanasta
    template_name = 'NombreCanasta_list.html'

    # def get_context_data(self,*args,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     especialidad = NombreCanasta.objects.all()
    #     context['NombreCanasta'] = especialidad
    #     return context

class NombreCanastaEdit(UpdateView):
    model = NombreCanasta
    form_class = NombreCanastaForm
    template_name = 'CostosCirugia/NombreCanasta_edit.html'
    success_url= reverse_lazy('NombreCanastaList')



class ConceptoHonorarioSalarioCrear(CreateView):
    model = ConceptoHonorarioSalario
    form_class = ConceptoHonorarioSalarioForm
    template_name = 'CostosCirugia/ConceptoHonorarioSalario_crear.html'
    success_url= reverse_lazy('ConceptoHonorarioSalarioCrear')

    def post(self,request,*args,**kwargs):
        form = ConceptoHonorarioSalarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

class ConceptoHonorarioSalarioList(ListView):
    model = ConceptoHonorarioSalario
    template_name = 'ConceptoHonorarioSalario_list.html'

    # def get_context_data(self,*args,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     obj = ConceptoHonorarioSalario.objects.all()
    #     context['ConceptoHonorarioSalario'] = obj
    #     return context

class ConceptoHonorarioSalarioEdit(UpdateView):
    model = ConceptoHonorarioSalario
    form_class = ConceptoHonorarioSalarioForm
    template_name = 'CostosCirugia/ConceptoHonorarioSalario_edit.html'
    success_url= reverse_lazy('ConceptoHonorarioSalarioList')



class ActividadCrear(CreateView):
    model = Actividad
    form_class = ActividadForm
    template_name = 'CostosCirugia/Actividad_crear.html'
    success_url= reverse_lazy('ActividadCrear')

    def post(self,request,*args,**kwargs):
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

class ActividadList(ListView):
    model = Actividad
    template_name = 'Actividad_list.html'

    # def get_context_data(self,*args,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     obj = ConceptoHonorarioSalario.objects.all()
    #     context['Actividad'] = obj
    #     return context

class ActividadEdit(UpdateView):
    model = Actividad
    form_class = ActividadForm
    template_name = 'CostosCirugia/Actividad_edit.html'
    success_url= reverse_lazy('ActividadList')



class ConstanteCrear(CreateView):
    model = Constante
    form_class = ConstanteForm
    template_name = 'CostosCirugia/Constante_crear.html'
    success_url= reverse_lazy('ConstanteCrear')

    def post(self,request,*args,**kwargs):
        form = ConstanteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

class ConstanteList(ListView):
    model = Constante
    template_name = 'Constante_list.html'

    # def get_context_data(self,*args,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     obj = Constante.objects.all()
    #     context['Constante'] = obj
    #     return context

class ConstanteEdit(UpdateView):
    model = Constante
    form_class = ConstanteForm
    template_name = 'CostosCirugia/Constante_edit.html'
    success_url= reverse_lazy('ConstanteList')