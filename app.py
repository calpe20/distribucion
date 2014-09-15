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

query = 'SELECT * FROM usuario'

cursor.execute(query)

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/usuario/<name>')
def usuarios(name=None):
	
if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)
