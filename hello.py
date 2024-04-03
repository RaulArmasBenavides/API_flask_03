from flask import Flask
from flask import request, render_template_string, render_template
app = Flask(__name__)

TEMPLATE = '''
<html>
<head><title> Hello {{ person.name }} </title></head>
<body> Hello FOO </body>
</html>
'''

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


@app.route('/hello-ssti')
def hello_ssti():
    person = {'name':"world", 'secret':'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='}
    if request.args.get('name'):
       person['name'] = request.args.get('name')
    # Replace FOO with person's name
    template = TEMPLATE.replace("FOO", person['name'])
    return render_template_string(template, person=person)


app.run(debug=True)