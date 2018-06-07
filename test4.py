from bs4 import BeautifulSoup
import csv
import urllib3

http = urllib3.PoolManager()
web2 = http.request('GET', 'https://www.reclamos.cl/entel_pcs/reclamo/2018/may/entel_sin_se_al_1')
soup = BeautifulSoup(web2.data, 'lxml') #Propiedad .data
reclamos = soup.select('body div span p') #Se agrega body y tbody para acotar las busquedas(
reclamos = str(reclamos)
reclamos = BeautifulSoup(reclamos, 'lxml').text
print (reclamos)
