#Framework flask
#En terminal py -3 -m venv venv para crear la carpeta venv
#ls para comprobarlo
# despues ejecutar: . venv/bin/activate ... 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask2 ‼"

@app.route("/test")
def test():
    return "Funciono el test"

@app.route("/test2")
def test2():
    return "Funciono el test2"

#Para generar ambiente de desarrollo debemos modificar la constante flask env: set FLASK_ENV=development
#con esto el servidor revisará los cambios a las rutas en cada momento que cambien