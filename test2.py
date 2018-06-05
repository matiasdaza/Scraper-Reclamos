from bs4 import BeautifulSoup
import csv
import urllib3

http = urllib3.PoolManager()

web = http.request('GET', 'https://www.reclamos.cl/telecomunicaciones?page=1')

soup = BeautifulSoup(web.data, 'lxml') #Propiedad .data
#titulo = soup.a.text

links = soup.select('body tbody a') #Se agrega body y tbody para acotar las busquedas


for link in links:
    urls = link.get('href') #sacamos uno a uno los links
    texto = link.get_text() #Sacamos el texto asociado al link
    salida = str(texto)+" "+str(urls)
    print(salida + "\n")
#print(titulo)
