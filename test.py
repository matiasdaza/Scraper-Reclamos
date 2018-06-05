# import urllib.request
import requests
import bs4 #beatiful soup
import sys


#r = urllib.request.urlopen('http://www.python.org')
#mybytes = r.read()

#mystr = mybytes.decode("utf8")
#r.close

res = requests.get('https://www.reclamos.cl/telecomunicaciones?page=1')
print(res.text)
#mystr = requests.post('http://www.python.org')
#myster = mystr[body]
#print(mystr.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')
hi = soup.select('tbody')

Titulo = hi[1].getText()
print(Titulo)
