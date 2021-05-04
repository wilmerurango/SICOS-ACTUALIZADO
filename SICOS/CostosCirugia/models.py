from django.db import models

# Create your models here.
class TipoProcedimiento(models.Model):
    nombre_tipo_proc = models.CharField('Nombre de la Especialidad', null = True, max_length = 80, unique=True)
    
    def __str__(self):
        return '%s' % (self.nombre_tipo_proc)
    
    class Meta:
        ordering = ['nombre_tipo_proc']



class NombreCanasta(models.Model):
    name_can = models.CharField('Nombre de la Canasta', null = True, max_length = 85, unique=True)
    
    def __str__(self):
        return '%s' % (self.name_can)
    
    class Meta:
        ordering = ['name_can']



class ConceptoHonorarioSalario(models.Model):
    nombre_concep_hon = models.CharField('Nombre del Concepto', null = True, max_length = 30, unique=True)
    
    def __str__(self):
        return '%s' % (self.nombre_concep_hon)
    
    class Meta:
        ordering = ['nombre_concep_hon']



class Actividad(models.Model):#aqui se escribe a q actividad pertenece el salario (entrada, ciruria, postcirugia, salida , etc)

    nombre_act = models.CharField('Nombre de la Actividad', null = True, max_length = 20, unique=True)
    
    def __str__(self):
        return '%s' % (self.nombre_act)
    
    class Meta:
        ordering = ['nombre_act']


class Constante(models.Model):
    iss_adicional = models.FloatField('Porcentaje Ganancia', null = True)
    valor_uvt = models.FloatField('Valor UVT Especialistas', null = True, default = 0)
    smdlv = models.FloatField('Salaraio Minimo Diario L.V.', null = True, default = 0)
    derecho_sala = models.FloatField('Derecho de Sala', null = True)
    estancia = models.FloatField('Estancia', null=True)
    
    def __str__(self):
        return '%s' % (self.iss_adicional)
    
    # class Meta:
    #     ordering = ['iss_adicional']


class TipoEstancia(models.Model):
    nombre_tipo_est = models.CharField('Tipo de Estancia', null =  True, max_length = 60)
    numero_camas = models.IntegerField('Número de Camas', null =  True, default = 0)

    def __str__(self):
        return '%s' % (self.nombre_tipo_est)


class Cargo(models.Model):
    salario='SALARIO'
    honorario_anes = 'HONORARIO ANESTESIOLOGIA'
    honorario_esp = 'HONORARIO ESPECIALISTA'
    consulta = 'CONSULTAS'
    opcion_choices=[
        (salario,'SALARIO'),
        (consulta,'CONSULTAS'),
        (honorario_anes,'HONORARIO ANESTESIOLOGIA'),
        (honorario_esp,'HONORARIO ESPECIALISTA'),
    ]
    tipoProcedimiento = models.ForeignKey(TipoProcedimiento,verbose_name = 'Especialidad', null = True, on_delete=models.PROTECT)
    tipo = models.CharField('Concepto',max_length=24,choices=opcion_choices, default=salario)
    nombre_cargo = models.CharField('Cargo', null = True, max_length = 30, unique=True)
    descripcion = models.CharField('Descripción de Cargo', null = True, max_length = 30)
    valor = models.FloatField('Costo por hora')

    def __str__(self):
        return '%s' % (self.nombre_cargo)


class Insumo(models.Model):
    desechable='DESECHABLE'
    medicamento = 'MEDICAMENTO'
    dispositivos_med='DISPOSITIVOS MEDICOS'
    paq_desechable = 'PAQUETE DESECHABLE'
    limpiezA = 'LIMPIEZA'
    paq_reutilizable = 'PAQUETE REUTILIZABLE'

    opcion_choices=[
        (desechable,'DESECHABLE'),
        (medicamento,'MEDICAMENTO'),
        (dispositivos_med,'DISPOSITIVOS MEDICOS'),
        (paq_desechable,'PAQUETE DESECHABLE'),
        (limpiezA,'LIMPIEZA'),
        (paq_reutilizable,'PAQUETE REUTILIZABLE'),
    ]

    nombre= models.CharField('Nombre del Insumo', null = True, max_length = 30, unique=True)
    conceptoInsumo = models.CharField('Concepto Insumo',max_length=20,choices=opcion_choices, default=medicamento)
    codigo = models.CharField('Codigo del Insumo', null = True, max_length = 30)
    presentacion = models.CharField('Presentación', null = True, max_length = 30)
    valor = models.FloatField('Valor Compra')

    def __str__(self):
        return '%s' % (self.nombre)


class Canasta(models.Model):
    nombreCanasta = models.ForeignKey(NombreCanasta, verbose_name ='Nombre de la Canasta', on_delete=models.PROTECT, null = True)
    actividad =  models.ForeignKey(Actividad, verbose_name ='Ubicación', null = True,blank=True, on_delete = models.PROTECT)
    insumo =  models.ForeignKey(Insumo, verbose_name ='Insumo', null = True,blank=True, on_delete = models.PROTECT)
    cantidad =  models.FloatField('Cantidad', null = True, default = 1)


class Procedimiento(models.Model):
    cod_cup = models.CharField('Código Cups', null = True, max_length = 20, blank = True)
    cod_soat = models.CharField('Código SOAT', null = True, max_length = 20, blank = True)
    tipoProcedimiento = models.ForeignKey(TipoProcedimiento,verbose_name = 'Especialidad', null = True, on_delete=models.PROTECT)
    nombre_proc = models.CharField('Nombre del Procedimiento', null = True, max_length = 190, unique=True)
    nombreCanasta = models.ForeignKey(NombreCanasta,verbose_name = 'Canasta', null = True, on_delete=models.PROTECT)
    duracion_proc = models.FloatField('Duración en minutos', null = True)
    uvr =  models.FloatField('UVR', null = True, blank = True, default = 0)
    conts_soat = models.FloatField('Constante SOAT', null = True, blank = True, default = 0)
    dias_estancia = models.IntegerField('Días Estancia', null = True, default = 0)
    
    def __str__(self):
        return '%s' % (self.nombre_proc)


class HonorarioSalario(models.Model):
    conceptoHonorarioSalario = models.ForeignKey(ConceptoHonorarioSalario,verbose_name = 'Concepto', null = True, on_delete=models.PROTECT)
    tipoProcedimiento = models.ForeignKey(TipoProcedimiento,verbose_name = 'Especialidad', null = True, on_delete=models.PROTECT)
    procedimiento = models.ForeignKey(Procedimiento,verbose_name = 'Procedimiento', null = True, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo,verbose_name = 'Cargo', null = True, on_delete=models.PROTECT)
    costo = models.FloatField('Costo no Paramertrizado', null = True, blank = True, default=0)
    actividad =  models.ForeignKey(Actividad, verbose_name ='Ubicación', null = True,blank=True, on_delete = models.PROTECT)
    def __str__(self):
        return '%s' % (self.cargo)

#este modelo es solo para consultar los procedimientos
class Consulta(models.Model):
    tipoProcedimiento = models.ForeignKey(TipoProcedimiento,verbose_name = 'Tipo Procedimiento', null = True, on_delete=models.CASCADE)
    procedimiento = models.ForeignKey(Procedimiento, verbose_name = 'Nombre del Procedimiento', null = True, on_delete = models.CASCADE)
    ganancia = models.FloatField('Ganancia', default = 0)
