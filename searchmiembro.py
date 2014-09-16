# -*- encoding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import nltk
import os

os.system('clear')
dni = '43517096'
url = "http://www.infogob.com.pe/ERM_2014/ficha.aspx?IdDni="+dni+"&IdTab=1"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

links = soup.find(id='content-datos-right')
pagina = links.findAll('td')
tds = []

limpio = []
a = 0
for dato in pagina:
	a += 1
	dato = dato.text
	if dato == ":" or dato == "DISTRITO" or dato == "MIEMBRO DE MESA" or a == 4 or a == 7 or a == 10:
		pass
	else:
		limpio.append(dato)
		print dato

print limpio
