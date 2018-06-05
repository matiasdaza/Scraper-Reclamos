from bs4 import BeautifulSoup
import csv
import urllib3


for i in range(1,2):
    http = urllib3.PoolManager()
    url1 = 'https://www.reclamos.cl/telecomunicaciones?page='+str(i)

    web = http.request('GET', url1)

    soup = BeautifulSoup(web.data, 'lxml') #Propiedad .data
    #titulo = soup.a.text

    links = soup.select('body tbody a') #Se agrega body y tbody para acotar las busquedas


    for link in links:
        direccion = link.get('href') #sacamos uno a uno los links
        texto = link.get_text() #Sacamos el texto asociado al link
        salida = str(texto)+" "+str(direccion)
        print(salida + "\n")
        url2 = str(direccion)
        web2 = http.request('GET', url2)
        soup = BeautifulSoup(web2.data, 'lxml') #Propiedad .data
        reclamo = soup.select('body div p') #Se agrega body y tbody para acotar las busquedas
        print(reclamos)
    #print(titulo)
