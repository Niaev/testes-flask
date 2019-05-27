# testes-flask

Esse repositório possui alguns exemplos de utilização do framework [Flask](flask.pocoo.org) para desenvolvimento *web* com **Python**. Pretendo incluir aqui exemplos básicos (baseados na sessão *[Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/#quickstart)*) até alguns exemplos mais complexos, para fins didáticos.

## Como usar

Para testar os exemplos, é necessário que você instale os [requisitos](#requisitos) e baixe o conteúdo desse repositório clicando em ```Clone or Download``` e em seguida em ```Download ZIP```, ou você pode cloná-lo, executando o seguinte comando em seu terminal:
```
$ git clone git://github.com/Niaev/testes-flask
```

### Requisito(s)
* [Flask](https://pypi.org/project/Flask/1.0.2/) - ```pip install Flask``` ou ```python -m pip install Flask```

### Rodando a aplicação

Com o(s) requisito(s) instalado(s), no terminal do seu sistema operacional, você deve trocar para o diretório do clone/conteúdo baixado e em seguida determinar uma variável de ambiente ```FLASK_APP```, que armazena o nome do arquivo da aplicação que deseja executar:
```
$ FLASK_APP=index.py
```
E então, executar o Flask:
```
$ flask run
```
ou
```
$ python -m flask run
```

### Testando

Vá para o seu navegador e digite na barra de pesquisas ```127.0.0.1:5000/``` e aperte ```Enter```.