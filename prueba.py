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

query = 'SELECT * FROM clientes LIMIT 1,10'

cursor.execute(query)

data = cursor.fetchall()

for client in data:
	print client[2]
