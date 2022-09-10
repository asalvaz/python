#Framework flask
#En terminal py -3 -m venv venv para crear la carpeta venv
#ls para comprobarlo
# despues ejecutar: . venv/scripts/activate 
# o tambien puede ser . venv/bin/activate ... 

# Despues de ejecutar venv inicializamos este archivo de la siguiente manera: set FLASK_APP=Flask.py
# posteriormente corremos el flask con el siguiente ocmando: flask run
# En windows las variables de entorno desde PowerShell se declaran de la siguiente manera:
# $env:FLASK_APP = "Flask.py"
# $env:FLASK_DEBUG = 1
# $env:FLASK_ENV -->  is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.



#cuando obtengamos los datos del formulario utilizaremos request en import.
#y podemos imprimirlo con print(request.form)

#Para generar la url se utiliza la funcion url_for 
#Para redireccionar se utiliza la funcion redirect
#Para regresar bloqueo de peticiones se utiliza la función abort
#Para abrir páginas de template es necesario utilizar la funcion render_template
from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

#conector de mysql en flask
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='gituser',
    password = 'L0ok4tm3#1',
    database='BaseDeDatos'
)
#argumento dictionary=True permite que no se ordene por sus indices sino por el nombre retornando un diccionario Nombre:elnombre
cursor = conexion.cursor(dictionary=True)

#cursor.execute("Select * from Usuario");


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", mensaje="Variable_Flask", href_css="estilo3.css")
#Lo que esta <> es una variable
@app.route("/db/<usuario>")
def test(usuario):
    return "Funciono el test" + usuario
#forjando enteros int:<var>
#Los metodos son las referencias que tenemos a la BDD 
#algunos metodos utilizados son GET, PUT, PUSH, PATCH & DELETE
@app.route("/post/<int:post_id>", methods=['GET'])
def get(post_id):
    return "usuario: " + str(post_id)
#pueden incluirse en la misma función separados por coma methods=['GET','PUT']
#y se obtiene la información en base a request.method.
@app.route("/post/<int:post_id>", methods=['POST'])
def post(post_id):
    return "usuario: " + str(post_id)
#if request.method == 'GET' ... retrurn "get" else return "es otro metodo"
@app.route("/post/<int:post_id>", methods=['PUT'])
def put(post_id):
    return "usuario: " + str(post_id)


#---------------------------------  
# curl -d "llave1=dato1&llave2=dato2" -X POST http://127.0.0.1:5000/post/1  
# curl -d [solicitudes] -X ['metodo'] [url]
# -d envía datos
# -X declara el metodo a utilizar
# metodo entre comilla simple

#El print imprime en la consola de venv / flesk, y 
#El return lo imprime en consola de GitBash o Navegador
@app.route("/testing2", methods=['POST', 'GET'])
def test2():
    #print(request.form)
    #Para redireccionar se utiliza el nombre de la función
    #if(request.form['llave1']):
        return redirect(url_for("post",post_id=1))
    #    return redirect(url_for("post",post_id=request.form['llave1']))
    #    print(request.form['llave1'])
    #else:
        return "Funciono el test2"

#Abortando peticiones:

#@app.route("/testing4")
#def test4():
#    abort(401)
#    return "Funciono el test3‼"

@app.route("/testing3")
def test3():
    cursor.execute("Select * from Usuario");
    usuarios = cursor.fetchall()
    print(usuarios)
    return render_template("index.html", usuarios=usuarios, mensaje="Variable_Flask", href_css="estilo3.css")

@app.route("/crear", methods=['GET', 'POST'])
def crear():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        edad = request.form["edad"]
        #La consulta se ejecuta separado con %s para evitar el full injection
        #ya que la herramienta de flesk se encarga de sanitizar las consultas
        sql = "insert into usuario (username, email, edad) values (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        conexion.commit()
        #El URL_FOR redirecciona al Nombre de la función: 
        #Aquí se demuestra cambiando /Testing3 como la ruta de acceso y Test3 como el nombre de la función
        #A continuación llamamos el url_for(function)
        return(redirect(url_for("test3")))
    return render_template('formulariocontacto.html')