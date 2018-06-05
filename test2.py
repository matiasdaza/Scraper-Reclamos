from bs4 import BeautifulSoup
import csv
import urllib3

http = urllib3.PoolManager()

web = http.request('GET', 'https://www.reclamos.cl/telecomunicaciones?page=1')

soup = BeautifulSoup(web.data, 'lxml') #Propiedad .data
#titulo = soup.a.text

links = soup.find_all('a')

for link in links:
    urls = link.get('href') 
    texto = link.get_text()
    salida = str(texto)+" "+str(urls)
    print(salida + "\n")
#print(titulo)
