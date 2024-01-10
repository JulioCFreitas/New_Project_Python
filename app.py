from http.client import HTTPException
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

# Método GET por ID
@server.get('/pessoas/<int:id>')
@spec.validate(resp=Response(HTTP_200=Pessoa))
def buscar_pessoas_id(id: int):
    """Buscar pessoa por ID no DB"""
    pessoa = database.search(Query().id == id)
    if not pessoa:
        return jsonify({'message': 'Pessoa not found!'}), 404
    return jsonify(pessoa[0])

# Método GET por ID
# @server.get('/pessoas/<int:id>')
# @spec.validate(resp=Response(HTTP_200=Pessoas))
# def buscar_pessoas_id(id):
#     """ Buscar pessoa por ID no DB"""
#     try:
#         pessoa = database.search(Query().id == id)[0]
#     except IndexError:
#         return {'message':'Pessoa not found!'}
#     return jsonify(pessoa)


#Metodo POST
@server.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def inserir_pessoa():
    """Inserir pessoa no DB"""
    body = request.context.body.dict()
    database.insert(body)
    return body 
 
# Método PUT
@server.put('/pessoas/<int:id>')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def editar_pessoa(id):
    """Editar pessoa pelo ID no DB"""
    pessoa_query = Query()
    body = request.context.body.dict()
    database.update(body, pessoa_query.id == id)
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