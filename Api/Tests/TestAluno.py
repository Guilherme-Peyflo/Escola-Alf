import unittest # importando modulo de teste
import sys
sys.path.append('../')
from Alunos import AlunosById # importando classe a ser testada

class Test_Aluno(unittest.TestCase): # classe herdada do módulo de teste
    def test_get_aluno(self):
        aluno = AlunosById()
        print(aluno.get(1))
        assert aluno.get(1), "Erro ao buscar Aluno" # retorna o resultaod do teste
    
if __name__ == "__main__": # executando teste
    unittest.main()