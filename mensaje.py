from db import get_db
import sqlite3


db = get_db()

db.row_factory = sqlite3.Row
filas = db.execute("SELECT * FROM mensajesV1").fetchall()
db.close()

mensajes = []
for item in filas:
     mensajes.append({k: item[k] for k in item.keys()})


#mensajes= [
#{'usuario':'Persona123', 'asunto':'Hola', 'mensaje':'Hola, un saludo especial'},
#{'usuario':'Luis-123', 'asunto':'Buenas noticias', 'mensaje':'Hola, un saludo especial'},
#{'usuario':'Maria567', 'asunto':'Saludos', 'mensaje':'Hola, un saludo especial'},
#{'usuario':'Carlos-1993', 'asunto':'Hola', 'mensaje':'Hola, un saludo especial'},
#{'usuario':'Usuario987', 'asunto':'Chao', 'mensaje':'Chao, nos vemos luego'}]

