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

datos=[]

menu=int(input("1.Mostrar Personas covid positivos,UCI,PCR\n2.Comparar personas covid positivos, UCI y PCR\n3.Mostrar tasa de positividad de una Region y un dia determinado\n4.Mostrar la tasa de positividad promedio de un Mes\n5.Mostrar la relacion entre cantidad de personas COVID positivo y la poblacion de la Region\n6\n7\n8\n9\nOpcion:"))

while menu!=10:
    if menu==1:
        f=input("ingrese la fecha:")
        r=input("ingrese Region (por nombre):")
        #Para Casos Nuevos     
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
            
        #Para UCI
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

        datos+= ("Pacientes UCI en la fecha es:", str(ucilista[regionn][2+posicionfecha]))
        datos+= ("El total de pacientes UCI a nivel pais es:", str(total))
        #Para PCR
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
        menu=int(input("1.Mostrar Personas covid positivos,UCI,PCR\n2.Comparar personas covid positivos, UCI y PCR\n3.Mostrar tasa de positividad de una Region y un dia determinado\n4.Mostrar la tasa de positividad promedio de un Mes\n5.Mostrar la relacion entre cantidad de personas COVID positivo y la poblacion de la Region\n6\n7\n8\n9\nOpcion:"))   

    if menu==2:
        f=input("ingrese la fecha:")
        r=input("ingrese Region (por nombre):")
        fechafinal = []
        fechafinal.append(f[5:7])

        fechafinal.append(f[0:4])

        fechafinal.append(f[8:10])

        año = int(fechafinal[0])
        año -=1
        fechafinal[0] = str(año)
        añopasado = "-".join(fechafinal)

    #Años anteriores Casos nuevos
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

    #Años anteriores UCI
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
        
    #Años anteriores PCR
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
            print()
        menu=int(input("1.Mostrar Personas covid positivos,UCI,PCR\n2.Comparar personas covid positivos, UCI y PCR\n3.Mostrar tasa de positividad de una Region y un dia determinado\n4.Mostrar la tasa de positividad promedio de un Mes\n5.Mostrar la relacion entre cantidad de personas COVID positivo y la poblacion de la Region\n6\n7\n8\n9\nOpcion:"))

    if menu==3:
        f=input("ingrese la fecha:")
        r=input("ingrese Region (por nombre):")
        regionn=1
        stop1=True
        while stop1:
            if r==casosnuevoslista[regionn][0]:
                stop1=False
            else:
                regionn+=1
        if f in casosnuevoslista[0]:    
            posicionfecha=casosnuevoslista[0].index(f)
            a=int(casosnuevoslista[regionn][posicionfecha])
            regionn=1
            stop1=True
            while stop1:
                if r==pcrlista[regionn][0]:
                    stop1=False
                else:
                    regionn+=1
            if f in pcrlista[0]:
                posicionfecha=pcrlista[0].index(f)
                
                b=int(pcrlista[regionn][posicionfecha])
                print()
                print("La tasa de positividad para la fecha",f,"fue del",a/b,"%")
            else:
                print("no existe examenes pcr en esa fecha no se puede determinar la tasa de positividad")
        else:
            print("no existe esta informacion")
        menu=int(input("1.Mostrar Personas covid positivos,UCI,PCR\n2.Comparar personas covid positivos, UCI y PCR\n3.Mostrar tasa de positividad de una Region y un dia determinado\n4.Mostrar la tasa de positividad promedio de un Mes\n5.Mostrar la relacion entre cantidad de personas COVID positivo y la poblacion de la Region\n6\n7\n8\n9\nOpcion:"))

    if menu==4:
        f=input("ingrese la fecha:")
        r=input("ingrese Region (por nombre):")
        casosnuevos= open("Casos-nuevos-totales-por-region.txt", "r")

        linea = casosnuevos.readline()
        casosnuevoslista = []
        while linea != "":
            casosnuevoslista.append(linea.split(","))
            linea = casosnuevos.readline()

        fechafinal = []

        fechafinal.append(f[0:4])
        fechafinal.append(f[5:7])
    #Para 31 dias
        if fechafinal[1] == "03":
            fechafinal.append("03")
            fechafinal ="-".join(fechafinal)
            regionn=1
            stop1=True
            while stop1:
                if r==casosnuevoslista[regionn][0]:
                    stop1=False
                else:
                    regionn+=1               
            posicionfecha=casosnuevoslista[0].index(fechafinal)

            stop1=True
            total= 0
            i=posicionfecha
            while stop1:
                total+= int(casosnuevoslista[regionn][i])
                i+=1
                if i >= posicionfecha+28:
                    stop1=False
            print("La tasa de positividad en la region",r,"durante el mes fue de", total/31,"\n")

            posicionfecha=casosnuevoslista[0].index(fechafinal)
            stop1=True
            total=0
            i=posicionfecha
            regionn=1
            while stop1:
                total+=int(casosnuevoslista[regionn][i])
                i += 1
                if i >=posicionfecha+29:
                    i=posicionfecha
                    regionn+=1
                if regionn>= len(casosnuevoslista)-1:
                    stop1=False
            print("La tasa de positividad total durante el mes a nivel país fue de", total/31,"\n")

    #Meses 31 dias
        if fechafinal[1]=="01" or fechafinal[1]=="05" or fechafinal[1]=="07" or fechafinal[1]=="08" or fechafinal[1]=="10" or fechafinal[1]=="12":
            fechafinal.append("01")
            fechafinal="-".join(fechafinal)
            regionn=1
            stop1=True
            while stop1:
                if r==casosnuevoslista[regionn][0]:
                    stop1=False
                else:
                    regionn+=1
            posicionfecha=casosnuevoslista[0].index(fechafinal)
            stop1=True
            total=0
            i=posicionfecha
            while stop1:
                total+=int(casosnuevoslista[regionn][i])
                i+=1
                if i >= posicionfecha+31:
                    stop1=False
            print("La tasa de positividad en la región durante el mes fue de", total/31,"\n")

            posicionfecha=casosnuevoslista[0].index(fechafinal)
            stop1=True
            total=0
            i=posicionfecha
            regionn=1
            while stop1:
                total+=int(casosnuevoslista[regionn][i])
                i += 1
                if i >=posicionfecha+31:
                    i =posicionfecha
                    regionn+=1
                if regionn>= len(casosnuevoslista)-1:
                    stop1=False
            print("La tasa de positividad total nivel país fue de",total/31)

    #Meses 30 dias
        if fechafinal[1] == "04" or fechafinal[1] == "06" or fechafinal[1] == "09" or fechafinal[1] == "11":
            fechafinal.append("01")
            fechafinal="-".join(fechafinal)
            regionn=1
            stop1=True
            while stop1:
                if r==casosnuevoslista[regionn][0]:
                    stop1=False
                else:
                    regionn+=1
                    
            posicionfecha=casosnuevoslista[0].index(fechafinal)
            stop1=True
            total=0
            i=posicionfecha
            while stop1:
                total+=int(casosnuevoslista[regionn][i])
                i += 1
                if i >=posicionfecha+30:
                    stop1=False
            print("La tasa de positividad en la región durante el mes fue de",total/30)

            posicionfecha=casosnuevoslista[0].index(fechafinal)
            stop1=True
            total=0
            i=posicionfecha
            regionn=1
            while stop1:
                total+=int(casosnuevoslista[regionn][i])
                i += 1
                if i >=posicionfecha+30:
                    i=posicionfecha
                    regionn+=1
                if regionn>= len(casosnuevoslista)-1:
                    stop1=False
            print("La tasa de positividad total nivel país fue de",total/30)

    #Meses de 28 dias
        if fechafinal[1] == "02":
            fechafinal.append("01")
            fechafinal ="-".join(fechafinal)

            regionn=1
            stop1=True
            while stop1:
                if r==casosnuevoslista[regionn][0]:
                    stop1=False
                else:
                    regionn+=1
            posicionfecha=casosnuevoslista[0].index(fechafinal)
            stop1=True
            total=0
            i =posicionfecha
            while stop1:
                total+=int(casosnuevoslista[regionn][i])
                i += 1
                if i >=posicionfecha+28:
                    stop1=False
            print("La tasa de positividad en la región durante el mes fue de",total/28)

            posicionfecha=casosnuevoslista[0].index(fechafinal)
            stop1=True
            total=0
            i=posicionfecha
            regionn=1
            while stop1:
                total+=int(casosnuevoslista[regionn][i])
                i += 1
                if i >=posicionfecha+28:
                    i =posicionfecha
                    regionn+=1
                if regionn>= len(casosnuevoslista)-1:
                    stop1=False
            print("tasa de positividad total nivel pais fue de",total/28)
    
    if menu==5:
        r=input("ingrese Region (por nombre):")
        regionn=1
        stop1=True
        while stop1:
            if r==casosnuevoslista[regionn][0]:
                stop1=False
            else:
                regionn+=1
    
        stop1=True
        total= 0
        i=1
        j=1
        while stop1:
            total+= int(casosnuevoslista[regionn][j])       
            j+=1
            if j > len(casosnuevoslista[regionn])-1:
                stop1=False
        print("la relacion de la region de ", r, "es de", int(ucilista[regionn][2])//total," es a 1")
        
        stop1=True
        total=0
        r=1
        j=1
        promedios=[]
        posicionpromedios=[]
        while r!= len(casosnuevoslista)-1:
            stop1=True
            while stop1:
                total+= int(casosnuevoslista[r][j])
                j+=1
                if j==len(casosnuevoslista[r]):
                    stop1=False
                    j=1
                    posicionpromedios.append([int(ucilista[r][2])//total,r])

                    promedios.append(int(ucilista[r][2])//total)
                    r+=1
                    total=0   
        posicionpromedios.sort(reverse=True)
        promedios.sort(reverse=True)
        sumapromedios=sum(promedios)
        i = 0
        while i < len(promedios):
            if posicionpromedios[i][0] > sumapromedios:
                print()
                print("mayor al promedio")
            if posicionpromedios[i][0] == sumapromedios:
                print()
                print("estan en el promedio")
            if posicionpromedios[i][0]< sumapromedios:
                print()
                print("menor al promedio")
            print("la relacion en la region",casosnuevoslista[posicionpromedios[i][1]][0],"es de",posicionpromedios[i][0]," es a 1")  
            i +=1
        print()