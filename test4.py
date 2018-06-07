from bs4 import BeautifulSoup
import csv
import urllib3
import re

http = urllib3.PoolManager()
web2 = http.request('GET', 'https://www.reclamos.cl/movistar/reclamo/2018/jun/movistar_no_funciona_despu_s_de_ciertas_horas')
soup = BeautifulSoup(web2.data, 'lxml') #Propiedad .data
reclamos = soup.select('body div span p') #Se agrega body y tbody para acotar las busquedas(
reclamos = str(reclamos)
reclamos = BeautifulSoup(reclamos, 'lxml').text
reclamos = re.sub(r'[\t\r\n]', '', reclamos)
print (reclamos)
