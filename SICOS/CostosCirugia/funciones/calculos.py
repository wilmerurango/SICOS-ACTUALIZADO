import copy as cp

class calculo():
    obj1 = {}
    obj2 = {}
    obj3 = {}
    obj4 = {}
    obj5 = {}
    obj6 = {}
    obj7 = {}
    obj8 = {}
    obj9 = {}
    obj10 = {}
    
    def __init__(self,
                 objeto1 = 0,
                 objeto2 = 0,
                 objeto3 = 0,
                 objeto4 = 0,
                 objeto5 = 0,
                 objeto6 = 0,
                 objeto7 = 0,
                 objeto8 = 0,
                 objeto9 = 0,
                 objeto10 = 0,
                 ):
        self.obj1 = objeto1
        self.obj2 = objeto2
        self.obj3 = objeto3
        self.obj4 = objeto4
        self.obj5 = objeto5
        self.obj6 = objeto6
        self.obj7 = objeto7
        self.obj8 = objeto8
        self.obj9 = objeto9
        self.obj10 = objeto10


    def resultado(self):
        # obj1 = nombre_canasta
        # obj2 = honorario
        # obj3 = consulta #
        # obj4 = canasta #
        # obj5 = HonorarioSalario #
        # obj6 = procedimientos #
        # obj7 = estancias
        # obj10 = constante #


        #CREAR UNA LISTA VACIA
        datos_obte = []
        
        #OBTENER EL REGISTRO DE LA ULTIMA CONSULTA
        consul_ultimo = self.obj3.last()#ultimo objeto del formulario de consulta (filtro de busqueda)
        print('consulta hecha: ',consul_ultimo)
        
        if consul_ultimo:

            #OBTENER NOMBRE CANASTA
            canasta_consultada = self.obj6.filter(nombreCanasta = consul_ultimo.procedimiento.nombreCanasta).first()
       
            #CALCULAR EL VALOR DE LOS CONCEPTOS DENTRO DE LA CANASTA
            canasta = self.obj4.filter(nombreCanasta = canasta_consultada.nombreCanasta)
            valor_desechable = 0
            valor_medicamento = 0
            dispositivos_medicos = 0
            valor_paquete_desechable = 0
            limpieza = 0
            valor_paquete_reutili = 0

            
            for i in canasta:
                if i.insumo.conceptoInsumo =="DESECHABLE":
                    valor_desechable += round(i.cantidad * i.insumo.valor * (1+consul_ultimo.ganancia/100))
                else:
                    if i.insumo.conceptoInsumo =="MEDICAMENTO":
                        valor_medicamento += round(i.cantidad * i.insumo.valor * (1+consul_ultimo.ganancia/100))
                    else:
                        if i.insumo.conceptoInsumo =="DISPOSITIVOS MEDICOS":
                            dispositivos_medicos += round(i.cantidad * i.insumo.valor * (1+consul_ultimo.ganancia/100))
                        else: 
                            if i.insumo.conceptoInsumo =="PAQUETE DESECHABLE":
                                valor_paquete_desechable += round(i.cantidad * i.insumo.valor * (1+consul_ultimo.ganancia/100))
                            else:
                                # if i.insumo.conceptoInsumo =="LIMPIEZA":
                                #     limpieza += i.cantidad * i.insumo.valor
                                # if i.insumo.conceptoInsumo =="PAQUETE REUTILIZABLE":
                                valor_paquete_reutili += round(i.cantidad * i.insumo.valor*(1+consul_ultimo.ganancia/100))
                

            #CALCULAR EL VALOR TOTAL DE LA CANASTA
            valor_canasta_total = valor_desechable + valor_medicamento + dispositivos_medicos + valor_paquete_desechable + limpieza + valor_paquete_reutili

            
            # derecho de sala
            dere_sala = round(self.obj10.derecho_sala*(canasta_consultada.duracion_proc/60)*(1+consul_ultimo.ganancia/100))
            
            #ESTANCIA
            estancia = round(self.obj10.estancia*canasta_consultada.dias_estancia*(1+consul_ultimo.ganancia/100))
            
            #calcular el valor de los salarios
            salario_fil = self.obj5.filter(tipoProcedimiento = consul_ultimo.tipoProcedimiento).filter(procedimiento = consul_ultimo.procedimiento)


            #AGREGAR LA DURACION DEL PROCEDMIENTO
            procedimient = self.obj6.filter(nombre_proc = consul_ultimo.procedimiento.nombre_proc).first()
            duracion = procedimient.duracion_proc


            # contadores
            salarios_tot = []
            consulta_tot = []
            honor_anes_tot = []
            honor_esp = []
            salario_total = 0
            consulta_total = 0
            maximo = 0
            

            for i in salario_fil:

                #capturar salarios
                if i.cargo.tipo=="SALARIO":
                    sal= []
                    sal.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                    salario_cal = round((duracion/60)*i.cargo.valor*(1+consul_ultimo.ganancia/100))
                    sal.append(salario_cal)
                    salarios_tot.append(sal)
                    salario_total += salario_cal
                    print('salario',salario_total)
                else:
                    #capturar consultas
                    if i.cargo.tipo=="CONSULTAS":
                        con= []
                        con.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                        consulta_cal = round(i.cargo.valor*(1+consul_ultimo.ganancia/100))
                        con.append(consulta_cal)
                        consulta_tot.append(con)
                        consulta_total += consulta_cal
                        print('consulta',consulta_total)
                    else:
                        #capturar honorarios anesteciologo
                        if i.cargo.tipo=="HONORARIO ANESTESIOLOGIA":
                            anestesia = []
                            anestesia.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                            anestesia.append(round(i.cargo.valor*(duracion/60)*(1+consul_ultimo.ganancia/100)))
                            honor_anes_tot.append(anestesia)
                            print('lista anesteciologia',anestesia)
                        else:
                            #capturar honorarios especialista
                            
                            if i.cargo.tipo=="HONORARIO ESPECIALISTA":
                                esp = []
                                if i.conceptoHonorarioSalario.nombre_concep_hon == "ISS PLENO":
                                    costo = round(procedimient.uvr*self.obj10.valor_uvt*(1+consul_ultimo.ganancia/100))
                                    esp.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                                    esp.append(costo)

                                    if costo > maximo:
                                        maximo = costo
                                else:
                                    if i.conceptoHonorarioSalario.nombre_concep_hon == "ISS + 10%":
                                        costo = round(procedimient.uvr*self.obj10.valor_uvt*1.10*(1+consul_ultimo.ganancia/100))
                                        esp.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                                        esp.append(costo)

                                        if costo > maximo:
                                            maximo = costo
                                    else:
                                        if i.conceptoHonorarioSalario.nombre_concep_hon == "SOAT - 20%":
                                            costo = round(procedimient.conts_soat*self.obj10.smdlv*0.8*(1+consul_ultimo.ganancia/100))
                                            esp.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                                            esp.append(costo)

                                            if costo > maximo:
                                                maximo = costo
                                        else:
                                            if i.conceptoHonorarioSalario.nombre_concep_hon == "SOAT - 10%":
                                                costo = round(procedimient.conts_soat*self.obj10.smdlv*0.9*(1+consul_ultimo.ganancia/100))
                                                esp.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                                                esp.append(costo)

                                                if costo > maximo:
                                                    maximo = costo
                                            else:
                                                if i.conceptoHonorarioSalario.nombre_concep_hon == "SOAT":
                                                    costo = round(procedimient.conts_soat*self.obj10.smdlv*(1+consul_ultimo.ganancia/100))
                                                    esp.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                                                    esp.append(costo)

                                                    if costo > maximo:
                                                        maximo = costo
                                                else:
                                                    if i.conceptoHonorarioSalario.nombre_concep_hon == "TARIFA DIFERENCIAL":
                                                        costo = round(i.costo*(1+consul_ultimo.ganancia/100))
                                                        esp.append(i.conceptoHonorarioSalario.nombre_concep_hon)
                                                        esp.append(costo)

                                                        if costo > maximo:
                                                            maximo = costo
                                honor_esp.append(esp)

            # canasta
            datos_obte.append(canasta_consultada)#0)--agregar nombre de canasta *
            datos_obte.append(canasta)#1)--agregar costo canasta *
            datos_obte.append(round(valor_desechable))#2)--agregar canasta desechable *
            datos_obte.append(round(valor_medicamento))#3)--agregar canasta medicamneto *
            datos_obte.append(round(dispositivos_medicos))#4)--agregar canasta dispositivos medicos *
            datos_obte.append(round(valor_paquete_desechable))#5)--agregar canasta paquetes desechables *
            datos_obte.append(round(limpieza))#6)--agregar canasta limpieza - ESTE SE ELIMINO, LO QUE CORRESPONDA A LIMPIEZA SE IRA COMO DESECHABLE 
            datos_obte.append(round(valor_paquete_reutili))#7)--agregar canasta paquete reutilizable *
            datos_obte.append(round(valor_canasta_total))#8)--agregar canasta total *
            datos_obte.append(round(dere_sala))#9)--agregar derecho a sala *

            # salarios honorarios
            datos_obte.append(salarios_tot)#10)--agregar lista "concepto-valor" de los salarios *
            datos_obte.append(consulta_tot)#11)--agregar lista "concepto-valor" de las consultas *
            datos_obte.append(honor_anes_tot)#12)--agregar lista "concepto-valor" del anesteciologo *
            datos_obte.append(honor_esp)#13)--agregar lista "concepto-valor" de los Honorarios de Especialistas *
            datos_obte.append(round(salario_total))#14)--agregar valor total de los salarios *
            datos_obte.append(round(consulta_total))#15)--agregar valor total de los consultas *
            datos_obte.append(duracion)#16)--agregar duracion procedimiento
            datos_obte.append(round(maximo))#17)--agregar el valor mas caro de los honorarios 
            datos_obte.append(round(estancia))#18)--agregar el valor total de la  estancia *

        return datos_obte
