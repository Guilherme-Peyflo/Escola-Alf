import unittest
import sys
sys.path.append('../')
from Alunos import AlunosById

class Test_Aluno(unittest.TestCase):
    def test_get_aluno(self):
        aluno = AlunosById()
        print(aluno.get(1))
        assert aluno.get(1), "Erro ao buscar Aluno"
    
if __name__ == "__main__":
    unittest.main()