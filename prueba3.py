menu=int(input("Ingrese 1 para mostrar total de personas con COVID,UCI,PCR y total de cada uno:")) 
pcr= open("Examenes-PCR-region.txt") 
casosnuevos=open("Casos-nuevos-totales-por-region.txt") 
uci=open("Pacientes-UCI-region.txt")
'''
lineaspcr =pcr.read() 
lineasuci=uci.read()
lineascasosnuevos=casosnuevos.read()
lineaspcr=lineaspcr.split(",")
lineasuci=lineasuci.split(",")
lineascasosnuevos=lineascasosnuevos.split(",") 
listapcr=[lineaspcr] 
listauci=[lineasuci] 
listacasosnuevos=[lineascasosnuevos]
'''
if menu==1:
    fechas = pcr.readline().split(',')
    datos = pcr.readlines()
    regiones = []
    for region in datos:
        regiones.append(region.split(','))
        
    f = input("Ingrese fecha: ")
    r = int(input("1 - >Arica, 2 - >Tarapaca, 3 - >Antofagasta, 4 - >Atacama, 5 - >Coquimbo, 6 - >Valparaiso, 7 - >Metropolitana, 8 - >O'Higgins, 9 - >Maule, 10 - >Ñuble, 11 - >"))
    i = 3
    while (i<len(fechas)):
        if f == fechas[i]:
                print(regiones[r-1][i])
        i = i + 1
    
    fechas2=uci.readline().split(",")
    datos2=uci.readlines()
    regiones2=[]
    for region in datos2:
        regiones2.append(region.split(','))
    j=3
    while (j<len(fechas2)):
        if f == fechas2[j]:
                print(regiones2[r-1][j])
        j = j + 1


    fechas3=casosnuevos.readline().split(",")
    datos3=casosnuevos.readlines()
    regiones3=[]
    for region in datos3:
        regiones3.append(region.split(','))
    acum=0
    p=1
    while (p<len(fechas3)):
        if f == fechas3[p]:
                print(regiones3[r-1][p])
                acum+=int(regiones3[r-1][p])    
                print(acum)
        p = p + 1