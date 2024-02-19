from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return 'hola mundo perú'

@app.route("/hello")
def hello():
    return 'Hola mundo q tal'


@app.route("/nosotros")
def nosotros():
    return 'Contactanos'