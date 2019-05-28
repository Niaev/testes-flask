# imports
from flask import Flask, request, redirect, render_template

# instancia
app = Flask(__name__)

# rota / (raíz)
@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html', req = request.method)

# rota /index (índice ou raíz)
@app.route('/index/')
def other_index():
    # localhost:5000/ e localhost:5000/index/, nesse caso, são a mesma coisa. No caso do /index/, o usuário é redirecionado ao /
    return redirect('/')

# rota /page1
@app.route('/page1/')
def page1():
    return render_template('pages.html', page = 1)

# rota /page2
@app.route('/page2/')
def page2():
    return render_template('pages.html', page = 2)

if __name__ == '__main__':
    app.run()