
f = open('101 - 145.csv', 'r')
w = open('insert.txt', 'w')
for linea in f.readlines():
    linea = linea.split(' ; ')
    print(linea)
    linea[3] = linea[3].replace('\'','')
    for i in range(0,len(linea)):
        linea[i]=linea[i].strip()Pa
    linea2 = "','".join(linea[1:len(linea)])
    linea3 = linea[0]+",'"+linea2
    #salida = "Insert into reclamoscl.telecomunicaciones values ("+linea3[:-1]+"','','');\n"
    #Paw.write(salida)
