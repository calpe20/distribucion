# -*- encoding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import nltk
import os

os.system('clear')
url = "http://www.infogob.com.pe/ERM_2014/ficha.aspx?IdDni=43517096&IdTab=1"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

links = soup.find(id='content-datos-right')
pagina = links.findAll('td')
tds = []

for link in pagina:
	texto = link.text
	tds.append(texto)
limpio = []
a = 0
for dato in tds:
	a += 1
	if dato == ":" or dato == "DISTRITO" or dato == "MIEMBRO DE MESA" or a == 4 or a == 7 or a == 10:
		pass
	else:
		limpio.append(dato)
		print dato

print limpio
