# imports
from flask import Flask, render_template, url_for

# instancia
app = Flask(__name__)

# rota /
@app.route('/')
def index():
    return render_template('index.html', css = url_for('static', filename = 'style.css'))

if __name__ == '__main__':
    app.run()