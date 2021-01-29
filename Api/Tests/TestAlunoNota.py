import unittest # importando modulo de teste
import sys
sys.path.append('../')
from Alunos import NotaAluno # importando classe a ser testada

class Test_Aluno_nota(unittest.TestCase): # classe herdada do módulo de teste
    def test_nota(self):
        aluno = NotaAluno()
        print(aluno.get(5))
        assert aluno.get(5), "Erro ao buscar Aluno" # retorna o resultaod do teste
    
if __name__ == "__main__": # executando teste
    unittest.main()