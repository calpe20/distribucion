# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import MySQLdb

db_host='192.168.1.41'
usuario = 'root'
clave	= 'root'
basedato= 'cfageren_prueba'

db = MySQLdb.connect(host=db_host, 
	user= usuario, 
	passwd=clave, 
	db=basedato)
	
cursor = db.cursor()

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/mapa')
def mapa():
	saludos ='Esperando'
	zoom = 15
	coordenadas = "-8.377651, -74.543964"
	return render_template('mapa.html', saludo = saludos, coordenadas=coordenadas, zoom=zoom)

@app.route('/clientes/<limite>')
def clientes(limite=None):
	query = 'SELECT * FROM clientes LIMIT '.str(limite)
	print query
		
	cursor.execute(query)
	data = cursor.fetchall()
	return render_template('clientes.html', data=data)

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)
