from bs4 import BeautifulSoup
import csv
import urllib3
import re  #Librería para eliminar saltos de linea en reclamos

f = open('Salida.csv', 'w', encoding='utf-8')
for i in range(137,500): #Los valores de range son (página inicial, página final)
    http = urllib3.PoolManager()
    url1 = 'https://www.reclamos.cl/telecomunicaciones?page='+str(i)

    web = http.request('GET', url1)

    soup = BeautifulSoup(web.data, 'lxml') #Propiedad .data
    #titulo = soup.a.text

    links = soup.select('body tbody a') #Se agrega body y tbody para acotar las busquedas


    for link in links: #Este for recorre todos los reclamos
        direccion = link.get('href') #sacamos uno a uno los links
        titulo = link.get_text() #Sacamos el texto asociado al link
        #salida = str(texto)+" "+str(direccion)
        #print('\n'+salida + "\n")
        url2 = str(direccion)
        web2 = http.request('GET', url2)
        soup = BeautifulSoup(web2.data, 'lxml') #Propiedad .data
        reclamos = soup.select('body div span p') #Se agrega body div span p para acotar las busquedas
        reclamos = str(reclamos)
        reclamos = BeautifulSoup(reclamos, 'lxml').text #Se agrega forma más limpia de sacar los reclamos
        reclamos = re.sub(r'[\t\r\n]', '', reclamos) #Para eliminar los saltos de linea en reclamos
        Fechas = soup.select('body div span')
        for Fecha in Fechas: #Busca la fecha del reclamo
          #direccion = link.get('href') #sacamos uno a uno los links
          texto = Fecha.get('content') #Sacamos el texto asociado al link

          if(str(texto) != 'None'):
              fecha = str(texto)

        numeros = soup.find_all('div', class_="node-info") #Se buscan los div con la clase especificada
        for numero in numeros: #Busca el número del reclamo
          #direccion = link.get('href') #sacamos uno a uno los links
          Dividir = numero.get_text()
          Dividir = Dividir.split(' ')
          NReclamo = Dividir[7]
          #print(NReclamo)
        salida = str(NReclamo)+' ; '+ fecha +' ; '+ str(titulo) +' ; '+str(reclamos)+' ; '+url2+'\n'
        f.write(salida)
        #print(salida)
        print(i) #Indica el número de página en el que se encuentra
    #print(titulo)
