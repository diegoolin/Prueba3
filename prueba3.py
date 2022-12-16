def funcion1(fecha, region, info): 
    """Mostrar por pantalla la cantidad de personas COVID positivos, pacientes en UCI y cantidad de
    examenes PCR en un dia determinado y los hasta esa fecha acumulados, para alguna region en#particular y nivel pais."""
    regionnumero = 1
    stop = True
    while stop:
        if region == casos_nuevos_por_region_lista[regionnumero][0]:
            stop= False
        else:
            regionnumero +=1

    fechaposicion = casos_nuevos_por_region_lista[0].index(fecha)
    stop = True
    suma = 0
    i = 1
    j = 1
    while stop:
        suma += int(casos_nuevos_por_region_lista[i][j])
      
        j+=1
        if j > fechaposicion:
            j = 1
            i+=1
        if i >= len(casos_nuevos_por_region_lista)-1:
            stop = False
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("casos covid en la fecha", casos_nuevos_por_region_lista[regionnumero][fechaposicion])
    print("total a nivel pais",suma)
    
    info += ("casos covid en la fecha", str(casos_nuevos_por_region_lista[regionnumero][fechaposicion]))
    info += ("total a nivel pais",suma)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #pacientes UCI
    regionnumero = 1
    stop = True
    while stop:
        if region == pacientes_UCI_lista[regionnumero][0]:
            stop= False
        else:
            regionnumero +=1
    fechaposicion = pacientes_UCI_lista[0].index(fecha)

    stop = True
    suma = 0

    i = 1
    j = 3
    while stop:
        suma += int(pacientes_UCI_lista[i][j])
      
        j+=1
        if j > fechaposicion:
            j = 3
            i+=1
        if i >= len(pacientes_UCI_lista):
            stop = False
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("pacientes UCI en la fecha", pacientes_UCI_lista[regionnumero][2+fechaposicion])
    print("el total de pacientes UCI hasta la fecha es", suma)

    info += ("pacientes UCI en la fecha", str(pacientes_UCI_lista[regionnumero][2+fechaposicion]))
    info += ("el total de pacientes UCI hasta la fecha es", str(suma))
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #examenes PCR
    regionnumero = 1
    stop = True
    while stop:
        if region == examen_PCR_lista[regionnumero][0]:
            stop= False
        else:
            regionnumero +=1
    fechaposicion = examen_PCR_lista[0].index(fecha)
        
    stop = True
    suma = 0

    i = 1
    j = 3
    while stop:
        if examen_PCR_lista[i][j] != "":
            suma += int(examen_PCR_lista[i][j])
      
        j+=1
        if j > fechaposicion:
            j = 3
            i+=1
        if i >= len(examen_PCR_lista):
            stop = False
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("examenes PCR en la fecha", examen_PCR_lista[regionnumero][fechaposicion])  
    print("el total de examenes PCR hasta la fecha es", suma)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

    info += ("el total de examenes PCR hasta la fecha es", str(suma))
    info += ("el total de examenes PCR hasta la fecha es", str(suma))
    return info

def funcion2(fecha, region):
    """Comparar la cantidad de personas COVID positivos, pacientes en UCI y cantidad de examenes
    PCR en un dia determinado con el mismo dia del añoo anterior (si se tiene la informacion). Esta
    informacion sera para alguna region en particular y a nivel pais."""
    
#------------------------------------------------------------------------------------------------------------------------------------------------------

    fechalista = []

    fechalista.append(fecha[0:4])
    fechalista.append(fecha[5:7])
    fechalista.append(fecha[8:10])
    año = int(fechalista[0])
    año -=1
    fechalista[0] = str(año)
    año_anterior = "-".join(fechalista)

#------------------------------------------------------------------------------------------------------------------------------------------------------
    if fecha in casos_nuevos_por_region_lista[0]:
        regionnumero = 1
        stop = True
        while stop:
            if region == casos_nuevos_por_region_lista[regionnumero][0]:
                stop= False
            else:
                regionnumero +=1
                
        fechaposicion = casos_nuevos_por_region_lista[0].index(fecha)
        stop = True
        suma = 0
        i = 1
        j = 1
        while stop:
            suma += int(casos_nuevos_por_region_lista[i][j])
        
            j+=1
            if j > fechaposicion:
                j = 1
                i+=1
            if i >= len(casos_nuevos_por_region_lista)-1:
                stop = False
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("casos covid en la fecha", casos_nuevos_por_region_lista[regionnumero][fechaposicion])
        print("total a nivel pais",suma)
    else: 
        print("la informacion de paciente UCI de esa fecha no existe")  
        
#------------------------------------------------------------------------------------------------------------------------------------------------------

    if año_anterior in casos_nuevos_por_region_lista[0]:
        fechaposicion = casos_nuevos_por_region_lista[0].index(año_anterior)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("casos covid en la fecha del año anterior es", casos_nuevos_por_region_lista[regionnumero][fechaposicion])
        stop = True
        suma = 0
        i = 1
        j = 1
        while stop:
            suma += int(casos_nuevos_por_region_lista[i][j])
        
            j+=1
            if j > fechaposicion:
                j = 1
                i+=1
            if i >= len(casos_nuevos_por_region_lista)-1:
                stop = False    
        print("total a nivel pais del año anterior",suma)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("la informacion de pacientes UCI de esta fecha del año anterior no existe")

#------------------------------------------------------------------------------------------------------------------------------------------------------
    #pacientes UCI
    if fecha in pacientes_UCI_lista[0]:
        regionnumero = 1
        stop = True
        while stop:
            if region == pacientes_UCI_lista[regionnumero][0]:
                stop= False
            else:
                regionnumero +=1
        fechaposicion = pacientes_UCI_lista[0].index(fecha)

        stop = True
        suma = 0

        i = 1
        j = 3
        while stop:
            suma += int(pacientes_UCI_lista[i][j])
        
            j+=1
            if j > fechaposicion:
                j = 3
                i+=1
            if i >= len(pacientes_UCI_lista)-1:
                stop = False
        print("pacientes UCI en la fecha", pacientes_UCI_lista[regionnumero][fechaposicion])
        print("el total de pacientes UCI hasta la fecha es", suma)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("la informacion de paciente UCI de esa fecha no existe")
        
#------------------------------------------------------------------------------------------------------------------------------------------------------

    if año_anterior in pacientes_UCI_lista[0]:
        fechaposicion = pacientes_UCI_lista[0].index(año_anterior)
        stop = True
        suma = 0

        i = 1
        j = 3
        while stop:
            suma += int(pacientes_UCI_lista[i][j])
        
            j+=1
            if j > fechaposicion:
                j = 3
                i+=1
            if i >= len(pacientes_UCI_lista):
                stop = False
        print("pacientes UCI en la fecha del año anterior es", pacientes_UCI_lista[regionnumero][fechaposicion])
        print("total a de pacientes UCI a nivel pais del año anterior es", suma)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("la informacion de esta fecha del año anterior no existe")
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #examenes PCR
    if fecha in examen_PCR_lista[0]:

        regionnumero = 1
        stop = True
        while stop:
            if region == examen_PCR_lista[regionnumero][0]:
                stop= False
            else:
                regionnumero +=1
            
        fechaposicion = examen_PCR_lista[0].index(fecha)
            
        stop = True
        suma = 0

        i = 1
        j = 3
        while stop:
            if examen_PCR_lista[i][j] != "":
                suma += int(examen_PCR_lista[i][j])
        
            j+=1
            if j > fechaposicion:
                j = 3
                i+=1
            if i >= len(examen_PCR_lista):
                stop = False

        print("examenes PCR en la fecha", examen_PCR_lista[regionnumero][fechaposicion])  
        print("el total de examenes PCR hasta la fecha es", suma)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("la informacion de examenes covid de esa fecha no existe")
        
#------------------------------------------------------------------------------------------------------------------------------------------------------

    if año_anterior in examen_PCR_lista[0]:
        fechaposicion = examen_PCR_lista[0].index(año_anterior)
        print("examenes PCR en la fecha del año anterior es", examen_PCR_lista[regionnumero][fechaposicion])
        stop = True
        suma = 0

        i = 1
        j = 3
        while stop:
            if examen_PCR_lista[i][j] != "":
                suma += int(examen_PCR_lista[i][j])
        
            j+=1
            if j > fechaposicion:
                j = 3
                i+=1
            if i >= len(examen_PCR_lista):
                stop = False
        print("el total de examenes PCR en el pais el año anterior es de", suma)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("la informacion de examenes covid de esa fecha en el año anterior no existe")
        
def funcion3(fecha, region):
    """Mostrar la tasa de positividad de un dia determinado. La tasa se calcula como la cantidad de
    personas COVID positivo dividido en la cantidad de examenes PCR realizados."""
    regionnumero = 1
    stop = True
    while stop:
        if region == casos_nuevos_por_region_lista[regionnumero][0]:
            stop= False
        else:
            regionnumero +=1
    if fecha in casos_nuevos_por_region_lista[0]:    
        fechaposicion = casos_nuevos_por_region_lista[0].index(fecha)
        x = int(casos_nuevos_por_region_lista[regionnumero][fechaposicion])
        regionnumero = 1
        stop = True
        while stop:
            if region == examen_PCR_lista[regionnumero][0]:
                stop= False
            else:
                regionnumero +=1
        print(casos_nuevos_por_region_lista[0][fechaposicion])
        if fecha in examen_PCR_lista[0]:
            fechaposicion = examen_PCR_lista[0].index(fecha)
            
            z = int(examen_PCR_lista[regionnumero][fechaposicion])
            print()
            print("la tasa de positividad es del",x/z,"%")
            print()
        else:
            print("no existe examenes pcr en esa fecha no se puede determinar la tasa de positividad")
    else:
        print("no existe esta informacion")
        print()

def funcion4(fecha, region):
    """Mostrar la tasa de positividad promedio de un mes determinado. La tasa se calcula como el
    promedio de la tasa de positividad de todos los dias del mes. Esta informacion sera para alguna
    region en particular y nivel pais."""
    
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    casos_nuevos_por_region = open("Casos-nuevos-totales-por-region.txt", "r")

    linea = casos_nuevos_por_region.readline()
    casos_nuevos_por_region_lista = []
    while linea != "":
        casos_nuevos_por_region_lista.append(linea.split(","))
        linea = casos_nuevos_por_region.readline()

    #------------------------------------------------------------------------------------------------------------------------------------------------------

    fechalista = []

    fechalista.append(fecha[0:4])
    fechalista.append(fecha[5:7])

    #------------------------------------------------------------------------------------------------------------------------------------------------------

    if fechalista[1] == "03":#31 dias
        fechalista.append("03")
        fechalista ="-".join(fechalista)
        regionnumero = 1
        stop = True
        while stop:
            if region == casos_nuevos_por_region_lista[regionnumero][0]:
                stop= False
            else:
                regionnumero +=1
                
        fechaposicion = casos_nuevos_por_region_lista[0].index(fechalista)
        stop = True
        suma = 0
        i = fechaposicion
        while stop:

            suma += int(casos_nuevos_por_region_lista[regionnumero][i])
        
            i += 1
            if i >= fechaposicion+28:
                stop = False
        print("tasa de positividad en la region durante el mes", suma/31)

    #------------------------------------------------------------------------------------------------------------------------------------------------------

        fechaposicion = casos_nuevos_por_region_lista[0].index(fechalista)
        stop = True
        suma = 0
        i = fechaposicion
        regionnumero = 1
        while stop:

            suma += int(casos_nuevos_por_region_lista[regionnumero][i])

            i += 1
            if i >= fechaposicion+29:
                i = fechaposicion
                regionnumero +=1
            if regionnumero >= len(casos_nuevos_por_region_lista)-1:
                stop = False
        print("tasa de positividad total en el mes nivel pais", suma/31)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    if fechalista[1] == "01" or fechalista[1] == "05" or fechalista[1] == "07" or fechalista[1] == "08" or fechalista[1] == "10" or fechalista[1] == "12": #31 dias
        fechalista.append("01")
        fechalista ="-".join(fechalista)
        regionnumero = 1
        stop = True
        while stop:
            if region == casos_nuevos_por_region_lista[regionnumero][0]:
                stop= False
            else:
                regionnumero +=1
                
        fechaposicion = casos_nuevos_por_region_lista[0].index(fechalista)
        stop = True
        suma = 0
        i = fechaposicion
        while stop:

            suma += int(casos_nuevos_por_region_lista[regionnumero][i])
        
            i += 1
            if i >= fechaposicion+31:
                stop = False
        print("tasa de positividad en la region durante el mes", suma/31)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

        fechaposicion = casos_nuevos_por_region_lista[0].index(fechalista)
        stop = True
        suma = 0
        i = fechaposicion
        regionnumero = 1
        while stop:

            suma += int(casos_nuevos_por_region_lista[regionnumero][i])

            i += 1
            if i >= fechaposicion+31:
                i = fechaposicion
                regionnumero +=1
            if regionnumero >= len(casos_nuevos_por_region_lista)-1:
                stop = False
        print("tasa de positividad total nivel pais", suma/31)
    #------------------------------------------------------------------------------------------------------------------------------------------------------


    if fechalista[1] == "04" or fechalista[1] == "06" or fechalista[1] == "09" or fechalista[1] == "11":#30 dias
        fechalista.append("01")
        fechalista ="-".join(fechalista)
        regionnumero = 1
        stop = True
        while stop:
            if region == casos_nuevos_por_region_lista[regionnumero][0]:
                stop= False
            else:
                regionnumero +=1
                
        fechaposicion = casos_nuevos_por_region_lista[0].index(fechalista)
        stop = True
        suma = 0
        i = fechaposicion
        while stop:

            suma += int(casos_nuevos_por_region_lista[regionnumero][i])
        
            i += 1
            if i >= fechaposicion+30:
                stop = False
        print("tasa de positividad en la region durante el mes", suma/30)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

        fechaposicion = casos_nuevos_por_region_lista[0].index(fechalista)
        stop = True
        suma = 0
        i = fechaposicion
        regionnumero = 1
        while stop:

            suma += int(casos_nuevos_por_region_lista[regionnumero][i])

            i += 1
            if i >= fechaposicion+30:
                i = fechaposicion
                regionnumero +=1
            if regionnumero >= len(casos_nuevos_por_region_lista)-1:
                stop = False
        print("tasa de positividad total nivel pais", suma/30)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    if fechalista[1] == "02":#28 dias

        fechalista.append("01")
        fechalista ="-".join(fechalista)
        regionnumero = 1
        stop = True
        while stop:
            if region == casos_nuevos_por_region_lista[regionnumero][0]:
                stop= False
            else:
                regionnumero +=1
                
        fechaposicion = casos_nuevos_por_region_lista[0].index(fechalista)
        stop = True
        suma = 0
        i = fechaposicion
        while stop:

            suma += int(casos_nuevos_por_region_lista[regionnumero][i])
        
            i += 1
            if i >= fechaposicion+28:
                stop = False
        print("tasa de positividad en la region durante el mes", suma/28)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

        fechaposicion = casos_nuevos_por_region_lista[0].index(fechalista)
        stop = True
        suma = 0
        i = fechaposicion
        regionnumero = 1
        while stop:

            suma += int(casos_nuevos_por_region_lista[regionnumero][i])

            i += 1
            if i >= fechaposicion+28:
                i = fechaposicion
                regionnumero +=1
            if regionnumero >= len(casos_nuevos_por_region_lista)-1:
                stop = False
        print("tasa de positividad total nivel pais", suma/28)

def funcion5(region):
    """Mostrar la relaci´on entre cantidad de personas COVID positivo y la poblaci´on de la regi´on.covid/poblacion
    Imprimir los datos de mayor a menor valor. Indicar adem´as cuales regiones est´an por sobre y bajo
    el valor a nivel pa´ıs."""
    
    regionnumero = 1
    stop = True
    while stop:
        if region == casos_nuevos_por_region_lista[regionnumero][0]:
            stop= False
        else:
            regionnumero +=1

#------------------------------------------------------------------------------------------------------------------------------------------------------
    
    stop = True
    suma = 0
    i = 1
    j = 1
    while stop:
        suma += int(casos_nuevos_por_region_lista[regionnumero][j])
        
        j+=1
        if j > len(casos_nuevos_por_region_lista[regionnumero])-1:
            stop = False
    print("la relacion de la region de ", region, "es de", int(pacientes_UCI_lista[regionnumero][2])//suma, " es a 1")
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
    
    stop = True
    suma = 0
    region = 1
    j = 1
    promedio = []
    promedioposicion = []
    while region != len(casos_nuevos_por_region_lista)-1:
        stop = True
        while stop:
            suma += int(casos_nuevos_por_region_lista[region][j])
            j+=1
            if j == len(casos_nuevos_por_region_lista[region]):
                stop = False
                j = 1
                promedioposicion.append([int(pacientes_UCI_lista[region][2])//suma, region])
                promedio.append(int(pacientes_UCI_lista[region][2])//suma)
                region +=1
                suma = 0   
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    promedioposicion.sort(reverse=True)
    promedio.sort(reverse=True)
    sumapromedio = sum(promedio)

    i = 0

    while i < len(promedio):
        if promedioposicion[i][0] > sumapromedio:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("mayor al promedio")
        if promedioposicion[i][0] == sumapromedio:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("estan en el promedio")
        if promedioposicion[i][0]< sumapromedio:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("menor al promedio")
        print("la relacion en la region" ,casos_nuevos_por_region_lista[promedioposicion[i][1]][0],"es de", promedioposicion[i][0]," es a 1")  
        i +=1
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

def funcion6():
    """Identificar y mostrar los 10 d´ıas de cada a˜no con mayor cantidad de personas COVID positivo.
    Esta informaci´on ser´a para alguna regi´on en particular y nivel pa´ıs."""
    x = 0

def funcion7():
    """Identificar y mostrar los 10 d´ıas de cada a˜no con mayor cantidad de pacientes en UCI. Esta
    informaci´on ser´a para alguna regi´on en particular y nivel pa´ıs."""
    x = 0

def funcion8():
    """Imprimir dos gr´aficas con * de los datos de personas COVID positivos en un mes determinado.
    Esta informaci´on ser´a para alguna regi´on en particular y nivel pa´ıs. De manera opcional pueden
    utilizar la librer´ıa ”matlibplot”para generar las gr´aficas1"""
    x = 0

def funcion9(nombrearchivo, info):
    """Finalizar an´alisis y generar archivo de salida que incorpore todas las consultas realizadas por el
    usuario. Se debe preguntar al usuario que nombre le dar´a al archivo de salida."""
    archivo = open(nombrearchivo, "w")
    archivo.write(info)

    archivo.close()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
casos_nuevos_por_region = open("Casos-nuevos-totales-por-region.txt", "r")


linea = casos_nuevos_por_region.readline()
linea.replace("\n", "")

casos_nuevos_por_region_lista = []
while linea != "":
    casos_nuevos_por_region_lista.append(linea.split(","))
    linea = casos_nuevos_por_region.readline()
    linea.replace("\n", "")
casos_nuevos_por_region.close() 

#------------------------------------------------------------------------------------------------------------------------------------------------------

pacientes_UCI = open("Pacientes-UCI-region.txt")

linea = pacientes_UCI.readline()
linea.replace("\n", "")

pacientes_UCI_lista = []
while linea != "":
    pacientes_UCI_lista.append(linea.split(","))
    linea = pacientes_UCI.readline()
    linea.replace("\n", "")
pacientes_UCI.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------

examen_PCR = open("Examenes-PCR-region.txt")

linea = examen_PCR.readline()
linea.replace("\n", "")

examen_PCR_lista = []
while linea != "":
    examen_PCR_lista.append(linea.split(","))
    linea = examen_PCR.readline()
    linea.replace("\n", "")
examen_PCR.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------

info = []

#------------------------------------------------------------------------------------------------------------------------------------------------------

print("-------MENU-------")
print("ingrese 1 para mostrar por pantalla la cantidad de personas COVID positivos, pacientes en UCI y cantidad de examenes PCR en un dia determinado y los hasta esa fecha acumulados")
print("ingrese 2 para Comparar la cantidad de personas COVID positivos, pacientes en UCI y cantidad de examenes PCR en un dia determinado con el mismo dia del año anterior")
print("ingrese 3 para Mostrar la tasa de positividad de un dia determinado")
print("ingrese 4 para Mostrar la tasa de positividad promedio de un mes determinado")
print("ingrese 5 para Mostrar la relacion entre cantidad de personas COVID positivo y la poblacion de la region")
print("ingrese 6 para")
print("ingrese 7 para")
print("ingrese 8 para")
print("ingrese 9 para")
n = int(input("escoga la opcion: "))

#------------------------------------------------------------------------------------------------------------------------------------------------------

terminar = True
while terminar:

#------------------------------------------------------------------------------------------------------------------------------------------------------

    if n == 1:
        fecha = input("ingrese la fecha: ")
        region = input("ingrese el nombre de la region: ")
        opcion1 = funcion1(fecha, region, info)
        print("-------MENU-------")
        print("ingrese 1 para")
        print("ingrese 2 para")
        print("ingrese 3 para")
        print("ingrese 4 para")
        print("ingrese 5 para")
        print("ingrese 6 para")
        print("ingrese 7 para")
        print("ingrese 8 para")
        print("ingrese 9 para")
        n = int(input("escoga la opcion: "))

#------------------------------------------------------------------------------------------------------------------------------------------------------

    if n == 2:
        fecha = input("ingrese la fecha: ")
        region = input("ingrese el nombre de la region: ")
        opcion2 = funcion2(fecha, region)
        print("-------MENU-------")
        print("ingrese 1 para")
        print("ingrese 2 para")
        print("ingrese 3 para")
        print("ingrese 4 para")
        print("ingrese 5 para")
        print("ingrese 6 para")
        print("ingrese 7 para")
        print("ingrese 8 para")
        print("ingrese 9 para")
        n = int(input("escoga la opcion: "))
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
    
    if n == 3:
        fecha = input("ingrese la fecha: ")
        region = input("ingrese el nombre de la region: ")
        opcion3 = funcion3(fecha, region)
        print("-------MENU-------")
        print("ingrese 1 para")
        print("ingrese 2 para")
        print("ingrese 3 para")
        print("ingrese 4 para")
        print("ingrese 5 para")
        print("ingrese 6 para")
        print("ingrese 7 para")
        print("ingrese 8 para")
        print("ingrese 9 para")
        n = int(input("escoga la opcion: "))

#------------------------------------------------------------------------------------------------------------------------------------------------------

    if n == 4:
        fecha =input("ingrese el año y el mes(2020-01): ")
        region = input("ingrese la region: ")
        opcion4 = funcion4(fecha, region)
        print("-------MENU-------")
        print("ingrese 1 para")
        print("ingrese 2 para")
        print("ingrese 3 para")
        print("ingrese 4 para")
        print("ingrese 5 para")
        print("ingrese 6 para")
        print("ingrese 7 para")
        print("ingrese 8 para")
        print("ingrese 9 para")
        n = int(input("escoga la opcion: "))
    
#------------------------------------------------------------------------------------------------------------------------------------------------------

    if n == 5:
        
        region = input("ingrese la region: ")
        opcion5 = funcion5(region)
        print("-------MENU-------")
        print("ingrese 1 para")
        print("ingrese 2 para")
        print("ingrese 3 para")
        print("ingrese 4 para")
        print("ingrese 5 para")
        print("ingrese 6 para")
        print("ingrese 7 para")
        print("ingrese 8 para")
        print("ingrese 9 para")
        n = int(input("escoga la opcion: "))
        
    if n == 6:
         x = 0

    if n == 7:
         x = 0

    if n == 8:
         x = 0

    if n == 9: 
        nombrearchivo = input("ingrese el nombre de su archivo:" )
        opcion9 = funcion9(nombrearchivo, info)
        terminar =False