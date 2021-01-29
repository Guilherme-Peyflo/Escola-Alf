from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from Alunos import Alunos, AlunosById, AlunoCreate, NotaAluno, Aprovados
from Provas import Provas, InserirProvas
from Provas_Alunos import Cadastrar_provaAluno, ProvasAlunos

import sqlite3

db = create_engine("sqlite:///C:\\Users\\guilh\\Desktop\\Projeto_Proway\\Alf\\dbalf")#caminho do banco de dados
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

#urls...
api.add_resource(Alunos, '/')
api.add_resource(AlunoCreate, '/novoAluno')
api.add_resource(AlunosById, '/aluno/<id>')
api.add_resource(InserirProvas, '/Cadastrar-Provas')
api.add_resource(Provas, '/Provas')
api.add_resource(Cadastrar_provaAluno, '/cadastro-prova-de-aluno')
api.add_resource(ProvasAlunos, '/provas-alunos')
api.add_resource(NotaAluno, '/media-aluno/<id>')
api.add_resource(Aprovados, '/aprovados')


if __name__ == "__main__":
    print(db.connect())
    app.run()