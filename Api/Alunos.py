from flask import Flask, request
from flask_restful import Resource
from sqlalchemy import create_engine

db = create_engine("sqlite:///C:\\Users\\guilh\\Desktop\\Projeto_Proway\\Alf\\dbalf")#caminho do banco de dados

class Alunos(Resource):
    def get(self):
        connect = db.connect()
        query = connect.execute("select * from Alunos")
        results = [dict(zip(list(query.keys()),i)) for i in query.cursor]
        return results


class AlunosById(Resource):
    def delete(self,id):
        connect = db.connect()
        query = connect.execute("delete from Alunos where id_aluno = {}".format(id))
        return {"message": "Aluno deletado"}

    def get(self, id):
        connect = db.connect()
        query = connect.execute('select * from Alunos where id_aluno = {}'.format(id))
        results = [dict(zip(list(query.keys()),i)) for i in query.cursor]
        return list(results)

    def put(self, id):
        connect = db.connect()
        nome = request.json['nome']
        connect.execute('update Alunos set nome = "{}" where id_aluno = {}'.format(nome, id))
        query = connect.execute('select * from Alunos where id_aluno = {}' .format(id))
        results = [dict(zip(list(query.keys()),i)) for i in query.cursor]
        return list(results)
    

class AlunoCreate(Resource):
    def post(self):
        connect = db.connect()
        search = connect.execute("select count(*) from Alunos")
        res_Search = [i for i in search.cursor]
        if res_Search[0][0] == 100:
            return {"message": "O limite de Alunos foi atingido. (100)"}
        nome = request.json['nome']
        connect.execute('insert into Alunos (nome) values ("{}")'.format(nome))
        query = connect.execute('select * from Alunos order by id_aluno desc limit 1')
        results = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return results


class NotaAluno(Resource):
    def get(self,id):
        connect = db.connect()
        query = connect.execute("select nome, nota_final from Alunos where id_aluno = {}".format(id))
        results = [dict(zip(list(query.keys()),i)) for i in query.cursor]
        return results

class Aprovados(Resource):
    def get(self):
        connect = db.connect()
        query = connect.execute("select nome, situacao from Alunos where situacao = 'Aprovado'")
        results = [dict(zip(list(query.keys()),i)) for i in query.cursor]
        return results
        


