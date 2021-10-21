from flask import Flask, render_template, blueprints, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db


main= blueprints.Blueprint('main', __name__)

@main.route( '/' )
def hello_world():
    """Función que maneja la raiz del sitio web.

        Parameters:
        Ninguno

        Returns:
        Plantilla index.html

    """

    return render_template('index.html')

@main.route('/login/', methods=['GET', 'POST'])
def login():
    """Función que maneja la ruta login.Responde a los métodos GET y POST.

        Parameters:
        Ninguno

        Returns:
        login.html si es invocada con el método GET. 
        Redirecciona a  main.ajax si es invocada con POST y la validación es verdadera.

    """

    if request.method =='POST':

        usuario = request.form['username']
        clave = request.form['userPassword']
        db = get_db()
        #sql = "select * from usuario where usuario = '{0}' and clave= '{1}'".format(usuario, clave)

        user = db.execute('select * from usuario where usuario = ? ', (usuario,)).fetchone()
        db.commit()
        db.close()

        if user is not None:
            sw = check_password_hash(user[4], clave)

            if(sw):
                return redirect(url_for('main.ajax'))

    return render_template('login.html')


@main.route('/registro/', methods=['GET', 'POST'])
def registro():
    """Función que maneja la ruta Registro.Responde a los métodos GET y POST.

        Parameters:
        Ninguno

        Returns:
        registro.html si es invocada con el método GET. 
        Crea un usuario en la BD si es invocada con POST, no tiene válidaciones.

    """

    if request.method == 'POST':

        nombre = request.form['nombre']
        usuario = request.form['username']
        correo = request.form['correo']
        clave = request.form['userPassword']

        db = get_db()
        clave = generate_password_hash(clave)
        db.execute("insert into usuario ( nombre, usuario, correo, clave) values( ?, ?, ?, ?)",(nombre, usuario, correo, clave))
        db.commit()
        db.close()
        



    return render_template('registro.html')



@main.route('/ajax/')
def ajax():
    """Función que maneja la ruta ajax.

        Parameters:
        Ninguno

        Returns:
        ajax.html 

    """
    return render_template('ajax.html')



