from typing import Optional
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel
from tinydb import TinyDB, Query


server = Flask(__name__)
spec = FlaskPydanticSpec('Flask', title='API PYTHON')
spec.register(server)
database = TinyDB('database.json')

class Pessoa(BaseModel):
    id: Optional[int]
    nome: str
    idade: int

class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int

#Metodo GET
@server.get('/pessoas')
@spec.validate(resp=Response(HTTP_200=Pessoas))
def buscar_pessoas():
    """ Busca todas pessoas no banco de dados"""
    return jsonify(
        Pessoas(
            pessoas=database.all(),
            count=len(database.all())
        ).dict()
    )

#Metodo POST
@server.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def inserir_pessoa():
    """ Insere uma pessoa no banco de dados"""
    body = request.context.body.dict()
    database.insert(body)
    return body 
 
#Metodo PUT
@server.put('/pessoas?<int:id>')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def editar_pessoa(id):
    """" Editar uma pessoa no banco de dados"""
    Pessoa = Query()

    body= request.context.body.dict()
    database.update(body, Pessoa.id == id)
    return jsonify(body)

server.run()