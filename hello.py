from flask import Flask, jsonify
from flask import request, render_template_string, render_template
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Mi API Flask',description='Una simple API demo')


# Definir un namespace
ns = api.namespace('demo', description='Operaciones demo')

# Modelo para el endpoint /submit
submit_model = api.model('SubmitModel', {
    'clave': fields.String(required=True, description='Clave de ejemplo'),
    'valor': fields.String(required=True, description='Valor de ejemplo')
})

api.add_namespace(ns)



@app.route("/")
@app.route("/index")
def index():
    return 'hola mundo perú'

@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        '''Devuelve un saludo básico'''
        return 'Hola mundo q tal'

@ns.route('/hello')
class HelloResource(Resource):
    def get(self):
        '''Devuelve un saludo básico'''
        return 'Hola mundo q tal'

@api.route('/nosotros')
class NosotrosResource(Resource):
    def get(self):
        '''Devuelve información de contacto'''
        return 'Contactanos'

@app.route("/test")
def test2():
    return 'esto es una prueba'

@app.route('/hello-insecure')
def hello_ssti_insecure():
    person = {'name':"world", 'secret':'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='}
    if request.args.get('name'):
        person['name'] = request.args.get('name')
    template = '<h2>Hello %s!</h2>' % person['name']
    return render_template_string(template, person=person)

@app.route('/hello-ssti2')
def hello_ssti2():
    person = {'name':"world", 'secret': 'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='}
    if request.args.get('name'):
        person['name'] = request.args.get('name')
    template = '<h2>Hello {{ person.name }} !</h2>'
    return render_template_string(template, person=person)

TEMPLATE = '''<html>
<head><title> Hello </title></head>
<div><h3>Prueba<h/3></div>
<body> Hello {{ person.name }}  </body>
</html>
'''

@app.route('/hello-ssti')
def hello_ssti():
    person = {'name':"world", 'secret':'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='}
    if request.args.get('name'):
       person['name'] = request.args.get('name')
    # Replace FOO with person's name
    # template = TEMPLATE.replace("FOO", person['name'])
    return render_template_string(TEMPLATE, person=person)

# @app.router('/suma/<int:num1>/<int:num2>')
# @app.router('/suma/<float:num1>/<int:num2>')
# @app.router('/suma/<float:num1>/<float:num2>')
# @app.router('/suma/<int:num1>/<float:num2>')
# def suma(num1 =0 ,num2= 0):
#     contexto = {'num1':num1, 'num2':num2}
#     return render_template("suma.html",**contexto)

@app.route('/submit', methods=['POST'])
def submit_data():
    # Asumiendo que los datos enviados son JSON
    data = request.json
    # Procesa tus datos aquí. Por ejemplo, imprimirlos en la consola.
    print(data)
    # Devuelve una respuesta
    return jsonify({"message": "Datos recibidos correctamente"}), 200

if __name__ =="__main__":
    app.run(debug=True)