# imports
from flask import Flask, render_template

# instancia
app = Flask(__name__)

# rota / (raíz)
@app.route('/')
@app.route('/<something>')
def index(something = None):
    # retorna o template (Flask procura na pasta 'templates' por padrão)
    return render_template("example_template.html", something=something)
    
    # digite algo na URL, após o '/' para ver o resultado
    # além disso, analise o template

if __name__ == '__main__':
    app.run()