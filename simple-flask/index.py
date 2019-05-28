# imports
from flask import Flask

# instância
app = Flask(__name__)

# rota / (raíz)
@app.route('/')
def index():
    # conteúdo HTML
    page_content = """
    <h1>simple-flask</h1>
    <h3>Seja bem-vindo(a) a minha aplicação simples utilizando Python e Flask</h3>

    <br>

    <p>Com o framework Flask é possível desenvolver aplicações web com a liguagem de programação Python. Para saber mais, <a href="flask.pocoo.org">clique aqui</a></p>
    """

    return page_content

if __name__ == '__main__':
    app.run()