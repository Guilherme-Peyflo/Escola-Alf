from flask import Flask, request
from flask_restful import Resource
from sqlalchemy import create_engine

db = create_engine("sqlite:///C:\\Users\\guilh\\Desktop\\Projeto_Proway\\Escola_Alf\\dbalf")


class Provas(Resource):
    def get(self):
        connect = db.connect()
        query = connect.execute("select * from Provas")
        results = [dict(zip(list(query.keys()),i)) for i in query.cursor]
        return results


class InserirProvas(Resource):
    def post(self):
        connect = db.connect()
        nomeProva = request.json['nomeProva']
        disc = request.json["disc"]
        q = request.json["q"]
        p = request.json["p"]
        for i in p:
            if type(i) != int or i < 0:
                return {"Message": "O peso da questão deve ser maior um número inteiro maior que 0"}
        connect.execute('insert into provas (nome_prova, materia, q1, peso_q1,q2, peso_q2, q3, peso_q3, q4, peso_q4, q5, peso_q5, q6, peso_q6, q7, peso_q7, q8, peso_q8, q9, peso_q9, q10, peso_q10) values ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(nomeProva, disc, q[0], p[0], q[1], p[1], q[2], p[2], q[3], p[3], q[4], p[4], q[5], p[5], q[6], p[6], q[7], p[7], q[8], p[8], q[9], p[9]))
        query = connect.execute('select * from provas order by id_prova desc limit 1')
        results = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return results

    

