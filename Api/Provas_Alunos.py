from flask import Flask, request
from flask_restful import Resource
from sqlalchemy import create_engine

db = create_engine("sqlite:///C:\\Users\\guilh\\Desktop\\Projeto_Proway\\Escola_Alf\\dbalf")

def avaliar(prova,gabarito,pesos):
    dividendo = 0
    divisor = 0
    for p,g,peso in zip(prova, gabarito,pesos):
        if p == g:
            dividendo = dividendo + 1 * peso
        divisor = divisor + peso
    nota_prova = dividendo/divisor
    nota_real = nota_prova * 10
    if nota_real == 10:
        nota_real = 9.9
    if nota_real == 0:
        nota_real = 1
    return nota_real

def calc_media(notas):
    nota_final = 0
    for nota in notas:
        nota_final = nota_final + nota[0]
    media = nota_final/len(notas)
    return media

def status(media):
    if media > 7:
        return "Aprovado"
    else:
        return "Reprovado"


class ProvasAlunos(Resource):
    def get(self):
        connect = db.connect()
        query = connect.execute("select * from provas_alunos")
        results = [dict(zip(list(query.keys()),i)) for i in query.cursor]
        return results

class Cadastrar_provaAluno(Resource):
    def post(self):
        connect = db.connect()
        idProva = request.json['idProva']
        idAluno = request.json["idAluno"]
        q = request.json["q"]
        gabarito = connect.execute("select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from provas where id_prova = {}".format(idProva))
        pesos = connect.execute("select peso_q1, peso_q2,peso_q3,peso_q4,peso_q5,peso_q6,peso_q7,peso_q8,peso_q9,peso_q10 from provas where id_prova = {}".format(idProva))
        lista_pesos = [p for p in pesos.cursor]
        lista_gabarito = [j for j in gabarito.cursor]
        nota = avaliar(q,lista_gabarito[0],lista_pesos[0])
        connect.execute('insert into provas_alunos (id_prova, id_doAluno, q1,q2, q3, q4, q5, q6, q7, q8, q9, q10, nota) values ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}" )'.format(idProva, idAluno, q[0],q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], nota))
        query = connect.execute("select * from provas_alunos order by id_provaAluno desc limit 1")
        result = [dict(zip(tuple(query.keys()),i)) for i in query.cursor]

        notas_aluno = connect.execute("select nota from provas_alunos where id_doAluno = {}".format(idAluno))
        list_notas = [n for n in notas_aluno.cursor]
        nota_final = calc_media(list_notas)
        print(nota_final)
        situacao = status(nota_final)
        print(situacao)
        final_query = connect.execute("update Alunos set nota_final = {:.2f}, situacao = '{}' where id_aluno = {}".format(nota_final, situacao,idAluno ))
        return result 

        






