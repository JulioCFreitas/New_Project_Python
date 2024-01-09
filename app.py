from flask import Flask

server = Flask(__name__)

@server.get('/pessoas')
def buscar_pessoas():
    return "retorno de uma pessoa"

server.run()