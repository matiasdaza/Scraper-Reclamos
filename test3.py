from bs4 import BeautifulSoup
import csv
import urllib3
''
http = urllib3.PoolManager()
url1 = 'https://www.reclamos.cl/claro/reclamo/2018/jun/claro_cuenta_pagada_y_no_me_lo_han_activado'

web = http.request('GET', url1)

soup = BeautifulSoup(web.data, 'lxml') #Propiedad .data
#titulo = soup.a.text

Fechas = soup.select('body div span') #Se agrega body y tbody para acotar las busquedas
for fecha in Fechas:
  #direccion = link.get('href') #sacamos uno a uno los links
  texto = fecha.get('content') #Sacamos el texto asociado al link
  #print(str(texto))
  if(str(texto) != 'None'):
      fecha = str(texto)
      print(fecha + '')
