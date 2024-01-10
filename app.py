from itertools import count
from typing import Optional
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query


server = Flask(__name__)
spec = FlaskPydanticSpec('Flask', title='API PYTHON')
spec.register(server)
database = TinyDB('database.json')
c = count()


#Classe Pessoa
class Pessoa(BaseModel):
    id: Optional[int] = Field(default_factory=lambda:next(c))
    nome: str
    idade: int

#Classe Pessoas
class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int

#Metodo GET
@server.get('/pessoas')
@spec.validate(resp=Response(HTTP_200=Pessoas))
def buscar_lista_pessoas():
    """ Buscar lista pessoa no DB"""
    return jsonify(
        Pessoas(
            pessoas=database.all(),
            count=len(database.all())
        ).dict()
    )

#Metodo GET
@server.get('/pessoas/<int:id>')
@spec.validate(resp=Response(HTTP_200=Pessoas))
def buscar_pessoas():
    """ Buscar pessoa pelo ID no DB"""
    return jsonify(
        Pessoas(
            pessoas=database.all(),
            count=len(database.all())
        ).dict()
    )

#Metodo POST
@server.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def inserir_pessoa():
    """Inserir pessoa no DB"""
    body = request.context.body.dict()
    database.insert(body)
    return body 
 
#Metodo PUT
@server.put('/pessoas/<int:id>')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def editar_pessoa(id):
    """Editar pessoa pelo ID no DB"""
    Pessoa = Query()
    body = request.context.body.dict()
    database.update(body, Pessoa.id == id)
    return jsonify(body)

#Metodo DELET
@server.delete('/pessoas/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def deletar_pessoa(id):
    """Deletar pessoa pelo ID no DB"""
    Pessoa = Query()
    database.remove(Pessoa.id == id)
    return jsonify({})

server.run()