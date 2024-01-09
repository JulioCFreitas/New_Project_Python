from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel

server = Flask(__name__)
spec = FlaskPydanticSpec('Flask', title='API PYTHON')
spec.register(server)

class Pessoa(BaseModel):
    id: int
    nome: str
    idade: int

@server.get('/pessoas')
@spec.validate(resp=Response(HTTP_200=Pessoa))
def buscar_pessoa():
    return "retorno de uma pessoa"

@server.post('/pessoas')
@spec.validate(body=Pessoa, resp=Response(HTTP_200=Pessoa))
def inserir_pessoa():
    body = request.context.body.dic
    return body 


server.run()