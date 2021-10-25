from db import get_db
import sqlite3


db = get_db()

db.row_factory = sqlite3.Row
filas = db.execute("SELECT * FROM mensajesV1").fetchall()
db.close()

mensajes = []
for item in filas:
     mensajes.append({k: item[k] for k in item.keys()})



