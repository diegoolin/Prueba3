def menu1(f,r,datos): 
    regionn = 1
    stop1 = True
    while stop1:
        if r == casosnuevoslista[regionn][0]:
            stop1= False
        else:
            regionn +=1

    posicionfecha = casosnuevoslista[0].index(f)
    stop1 = True
    total = 0
    i = 1
    j = 1
    while stop1:
        total += int(casosnuevoslista[i][j])
      
        j+=1
        if j > posicionfecha:
            j = 1
            i+=1
        if i >= len(casosnuevoslista)-1:
            stop1 = False
    print()

    print("Los casos positivos en la fecha es:", casosnuevoslista[regionn][posicionfecha])
    print("El total a nivel pais es:",total)
    
    datos += ("Casos covid en la fecha", str(casosnuevoslista[regionn][posicionfecha]))
    datos += ("Total a nivel pais",total)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #pacientes UCI
    regionn = 1
    stop1 = True
    while stop1:
        if r == ucilista[regionn][0]:
            stop1= False
        else:
            regionn +=1
    posicionfecha = ucilista[0].index(f)

    stop1 = True
    total = 0
    i = 1
    j = 3
    while stop1:
        total += int(ucilista[i][j])
      
        j+=1
        if j > posicionfecha:
            j = 3
            i+=1
        if i >= len(ucilista):
            stop1 = False
    print()
    print("Pacientes UCI en la fecha es:", ucilista[regionn][2+posicionfecha])
    print("El total de pacientes UCI a nivel pais es:", total)

    datos += ("Pacientes UCI en la fecha es:", str(ucilista[regionn][2+posicionfecha]))
    datos += ("El total de pacientes UCI a nivel pais es:", str(total))
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #examenes PCR
    regionn = 1
    stop1 = True
    while stop1:
        if r == pcrlista[regionn][0]:
            stop1= False
        else:
            regionn +=1
    posicionfecha = pcrlista[0].index(f)
        
    stop1 = True
    total = 0
    i = 1
    j = 3
    while stop1:
        if pcrlista[i][j] != "":
            total += int(pcrlista[i][j])     
        j+=1
        if j > posicionfecha:
            j = 3
            i+=1
        if i >= len(pcrlista):
            stop1 = False
    print()

    print("Los examenes PCR en la fecha es:", pcrlista[regionn][posicionfecha])  
    print("El total de examenes PCR a nivel pais es:", total)
    print()
    datos += ("El total de examenes PCR a nivel pais es:", str(total))
    datos += ("El total de examenes PCR a nivel pais es:", str(total))
    return datos
def menu2(f,r):
    """Comparar la cantidad de personas COVID positivos, pacientes en UCI y cantidad de examenes
    PCR en un dia determinado con el mismo dia del añoo pasado (si se tiene la informacion). Esta
    informacion sera para alguna region en particular y a nivel pais."""   

    fechafinal = []

    fechafinal.append(f[0:4])

    fechafinal.append(f[5:7])

    fechafinal.append(f[8:10])

    año = int(fechafinal[0])
    año -=1
    fechafinal[0] = str(año)
    añopasado = "-".join(fechafinal)

    if f in casosnuevoslista[0]:
        regionn=1
        stop1=True
        while stop1:
            if r==casosnuevoslista[regionn][0]:
                stop1= False
            else:
                regionn+=1
                
        posicionfecha=casosnuevoslista[0].index(f)
        stop1=True
        total=0
        i=1
        j=1
        while stop1:
            total+= int(casosnuevoslista[i][j])
            j+=1
            if j > posicionfecha:
                j=1
                i+=1
            if i >= len(casosnuevoslista)-1:
                stop1=False
        print()
        print("Los casos positivos en la fecha es:", casosnuevoslista[regionn][posicionfecha])
        print("Total a nivel pais de Casos positivos es:",total)
    else:
        print("La informacion de Casos positivos de esa fecha no existe")  
        

    if añopasado in casosnuevoslista[0]:
        posicionfecha = casosnuevoslista[0].index(añopasado)
        print()
        print("Los casos positivos en la fecha del año pasado es:", casosnuevoslista[regionn][posicionfecha])
        stop1=True
        total=0
        i=1
        j=1
        while stop1:
            total+=int(casosnuevoslista[i][j])       
            j+=1
            if j > posicionfecha:
                j=1
                i+=1
            if i >= len(casosnuevoslista)-1:
                stop1=False    
        print("Total nivel pais año pasado",total)
    else:
        print("La informacion de pacientes Casos positivos de esta fecha del año pasado no existe")
        print()

#------------------------------------------------------------------------------------------------------------------------------------------------------
    #pacientes UCI
    if f in ucilista[0]:
        regionn=1
        stop1=True
        while stop1:
            if r==ucilista[regionn][0]:
                stop1=False
            else:
                regionn+=1
        posicionfecha=ucilista[0].index(f)
        stop1=True
        total= 0
        i = 1
        j = 3
        while stop1:
            total+=int(ucilista[i][j]) 
            j+=1
            if j > posicionfecha:
                j = 3
                i+=1
            if i >= len(ucilista)-1:
                stop1=False
        print("La cantidad de pacientes UCI en la fecha es:", ucilista[regionn][posicionfecha])
        print("el total de pacientes UCI a nivel pais es:", total)
    else:
        print("La informacion de pacientes UCI de esa fecha no existe")
        
#------------------------------------------------------------------------------------------------------------------------------------------------------

    if añopasado in ucilista[0]:
        posicionfecha = ucilista[0].index(añopasado)
        stop1=True
        total=0
        i = 1
        j = 3
        while stop1:
            total+= int(ucilista[i][j])
            j+=1
            if j > posicionfecha:
                j=3
                i+=1
            if i >= len(ucilista):
                stop1=False
        print("La cantidad de pacientes UCI en la fecha del año pasado es:",ucilista[regionn][posicionfecha])
        print("total de pacientes UCI a nivel pais del año pasado es:",total)       
        print()
    else:
        print("La informacion de esta fecha del año pasado no existe")
        print()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #examenes PCR
    if f in pcrlista[0]:
        regionn=1
        stop1=True
        while stop1:
            if r==pcrlista[regionn][0]:
                stop1=False
            else:
                regionn+=1
            
        posicionfecha=pcrlista[0].index(f)
            
        stop1=True
        total=0

        i = 1
        j = 3
        while stop1:
            if pcrlista[i][j]!= "":
                total= int(pcrlista[i][j])       
            j+=1
            if j > posicionfecha:
                j = 3
                i+=1
            if i >= len(pcrlista):
                stop1= False

        print("PCR en la fecha es:",pcrlista[regionn][posicionfecha])  
        print("El total de PCR a nivel pais es:",total)       
    else:
        print("La informacion de PCR de esa fecha no existe")
        
#------------------------------------------------------------------------------------------------------------------------------------------------------

    if añopasado in pcrlista[0]:
        posicionfecha = pcrlista[0].index(añopasado)
        print("examenes PCR en la fecha del año pasado es", pcrlista[regionn][posicionfecha])
        stop1= True
        total=0
        i = 1
        j = 3
        while stop1:
            if pcrlista[i][j] != "":
                total=int(pcrlista[i][j])
            j+=1
            if j > posicionfecha:
                j=3
                i+=1
            if i >= len(pcrlista):
                stop1=False
        print("El total de PCR en el pais el año pasado es de", total)
        print()
    else:
        print("la informacion de examenes covid de esa fecha en el año pasado no existe")



casosnuevos=open("Casos-nuevos-totales-por-region.txt", "r")
linea = casosnuevos.readline()
linea.replace("\n", "")
casosnuevoslista = []
while linea != "":
    casosnuevoslista.append(linea.split(","))
    linea = casosnuevos.readline()
    linea.replace("\n", "")
casosnuevos.close() 

uci= open("Pacientes-UCI-region.txt")
linea = uci.readline()
linea.replace("\n", "")
ucilista= []
while linea != "":
    ucilista.append(linea.split(","))
    linea = uci.readline()
    linea.replace("\n", "")
uci.close()

pcr= open("Examenes-PCR-region.txt")
linea = pcr.readline()
linea.replace("\n", "")
pcrlista= []
while linea != "":
    pcrlista.append(linea.split(","))
    linea = pcr.readline()
    linea.replace("\n", "")
pcr.close()


datos = []

menu=int(input("1\n2\n3\n4\n5\n6\n7\n8\n9\nOpcion:"))

fin = True
while fin:
    if menu==1:
        f=input("ingrese la fecha:")
        r=input("ingrese Region (por nombre):")
        uno=menu1(f,r,datos)
        menu=int(input("1\n2\n3\n4\n5\n6\n7\n8\n9\nOpcion:"))
    if menu==2:
        f=input("ingrese la fecha:")
        r=input("ingrese Region (por nombre):")
        dos=menu2(f,r)
        menu=int(input("1\n2\n3\n4\n5\n6\n7\n8\n9\nOpcion:"))
