import unittest
import sys
sys.path.append('../')
from Alunos import NotaAluno

class Test_Aluno_nota(unittest.TestCase):
    def test_nota(self):
        aluno = NotaAluno()
        print(aluno.get(5))
        assert aluno.get(5), "Erro ao buscar Aluno"
    
if __name__ == "__main__":
    unittest.main()