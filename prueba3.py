def menu1(f,r,i):
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
    i=1
    j=3
    while stop1:
        if pcrlista[i][j]!="":
            total+=int(pcrlista[i][j])
        j+=1
        if j>posicionfecha:
            j=3
            i+=1
        if i>=len(pcrlista):
            stop1=False
    print()        
    print("hasta la fecha de PCR:",pcrlista[regionn][posicionfecha])
    print("PCR nivel pais:",total)
    i+=("Hasta la fecha el total nivel pais de PCR es:",str(total))

    regionn=1
    stop1=True
    while stop1:
        if r==ucilista[regionn][0]:
            stop1=False
        else:
            regionn+=1
    posicionfecha=ucilista[0].index(f)
    stop1=True
    total=0
    i=1
    j=1
    while stop1:
        total+=int(ucilista[i][j])
        j+=1
        if j>posicionfecha:
            j=3
            i+=1
        if i>=len(ucilista):
            stop1=False
    print("en la fecha pacientes UCI es:",ucilista[regionn][posicionfecha+2])
    print("total hasta la fecha UCI:",total)
    i+=("en la fecha pacientes UCI es:",str(ucilista[regionn][posicionfecha+2]))
    i+=("total hasta la fecha UCI:",str(total))

    regionn=1
    stop1=True
    while stop1:
        if r==casosnuevoslista[regionn][0]:
            stop1=False
        else:
            regionn+=1
    posicionfecha=casosnuevoslista[0].index(f)
    stop1=True
    total=0
    i=1
    j=1
    while stop1:
        total+=int(casosnuevoslista[i][j])
        j+=1
        if j>posicionfecha:
            j=1
            i+=1
        if i>=len(casosnuevoslista)-1:
            stop1=False
    print("Casos positivos en la fecha es:",casosnuevoslista[regionn][posicionfecha])
    print("nivel pais:",total)
    i+=("Casos positivos en la fecha es:",str(casosnuevoslista[regionn][posicionfecha]))
    i+=("Pais",total)
    return i


def menu2(f, r):
    fechafinal= []

    fechafinal.append(f[0:4])

    fechafinal.append(f[5:7])

    fechafinal.append(f[8:10])

    año = int(fechafinal[0])
    año -=1

    fechafinal[0] = str(año)
    añopasado = "-".join(fechafinal)

    if f in pcrlista[0]:
        regionn=1
        stop1= True
        while stop1:
            if r ==pcrlista[regionn][0]:
                stop1=False
            else:
                regionn+=1   
        posicionfecha = pcrlista[0].index(f)
            
        stop1=True
        total=0
        i = 1
        j = 3
        while stop1:
            if pcrlista[i][j]!= "":
                total+=int(pcrlista[i][j])
            j+=1
            if j > posicionfecha:
                j=3
                i+=1
            if i >= len(pcrlista):
                stop1=False

        print("PCR en la fecha es:",pcrlista[regionn][posicionfecha])  
        print("total de PCR hasta la fecha es",total)
        print()
    else:
        print("No existen datos en esa fecha")
        

    if añopasado in pcrlista[0]:
        posicionfecha = pcrlista[0].index(añopasado)
        print()
        print("PCR en la fecha del año anterior es", pcrlista[regionn][posicionfecha])
        stop1=True
        total= 0
        i=1
        j=3
        while stop1:
            if pcrlista[i][j]!="":
                total+=int(pcr[i][j])
        
            j+=1
            if j > posicionfecha:
                j=3
                i+=1
            if i >= len(pcrlista):
                stop1=False    
        print("total PCR el año pasado nivel pais",total)
        print()
    else:
        print("No existen los datos del año pasado de examenes PCR")
    
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

        i=1
        j=3
        while stop1:
            total+= int(ucilista[i][j])
            j+=1
            if j > posicionfecha:
                j=3
                i+=1
            if i >= len(ucilista)-1:
                stop1=False
        print("pacientes UCI en la fecha",ucilista[regionn][posicionfecha])
        print("el total de pacientes UCI hasta la fecha es",total)
        print()
    else:
        print("No existen los datos de esa fecha de pacientes UCI")
    
    if añopasado in ucilista[0]:
        posicionfecha=ucilista[0].index(añopasado)
        stop1=True
        total=0

        i = 1
        j = 3
        while stop1:
            total+=int(ucilista[i][j])
        
            j+=1
            if j > posicionfecha:
                j=3
                i+=1
            if i >= len(ucilista):
                stop1=False
        print("UCI en la fecha del año pasado es",ucilista[regionn][posicionfecha])
        print("Pais total pacientes UCI año pasado",total)
        print()
    else:
        print("La informacion de esta fecha del año pasado no existe")
    
    if f in casosnuevoslista[0]:
        regionn=1
        stop1=True
        while stop1:
            if r==casosnuevoslista[regionn][0]:
                stop1=False
            else:
                regionn+=1
                
        posicionfecha=casosnuevoslista[0].index(f)
        stop1=True
        total=0
        i = 1
        j = 1
        while stop1:
            total+=int(casosnuevoslista[i][j])
            j+=1
            if j >posicionfecha:
                j=1
                i+=1
            if i >= len(casosnuevoslista)-1:
                stop1=False
        print()

        print("Casos nuevos en la fecha",casosnuevoslista[regionn][posicionfecha])
        print("Total a nivel pais de casos nuevos",total)
    else: 
        print("Informacion de paciente UCI de esa fecha no existe")

    if añopasado in casosnuevoslista[0]:
        posicionfecha=casosnuevoslista[0].index(añopasado)
        print()
        print("casos positivos en la fecha del año pasado es:",casosnuevoslista[regionn][posicionfecha])
        stop1=True
        total=0
        i = 1
        j = 1
        while stop1:
            total+= int(casosnuevoslista[i][j])
        
            j+=1
            if j >posicionfecha:
                j=1
                i+=1
            if i >= len(casosnuevoslista)-1:
                stop1=False    
        print("total a nivel pais de casos nuevos del año pasado",total)
        print()
    else:
        print("Informacion de pacientes UCI de esta fecha del año pasado no existe")    
    

    


pcr= open("Examenes-PCR-region.txt") 
casosnuevos=open("Casos-nuevos-totales-por-region.txt") 
uci=open("Pacientes-UCI-region.txt")
pcrlista=[]
ucilista=[]
casosnuevoslista=[]

lineas=pcr.readline()
lineas.replace("\n","")
while lineas!="":
    pcrlista.append(lineas.split(","))
    lineas=pcr.readline()
    lineas.replace("\n","")
pcr.close()

lineas=uci.readline()
lineas.replace("\n","")
while lineas!="":
    ucilista.append(lineas.split(","))
    lineas=uci.readline()
    lineas.replace("\n","")
uci.close()

lineas=casosnuevos.readline()
lineas.replace("\n","")
while lineas!="":
    casosnuevoslista.append(lineas.split(","))
    lineas=casosnuevos.readline()
    lineas.replace("\n","")
casosnuevos.close()

i=[]
menu=int(input("1\n2\n3\n4\n5\n6\n7\n8\n9\nOpcion:"))
fin=True
while fin:
    if menu==1:
        f=input("Ingrese fecha:")
        r=input("Ingrese region (por nombre):")
        menuuno=menu1(f,r,i)
        menu=int(input("1\n2\n3\n4\n5\n6\n7\n8\n9\nOpcion:"))