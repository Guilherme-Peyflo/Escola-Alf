# Escola-Alf

O projeto foi feito em:

 - Python
 - Flask
 - SQlite
 Executar o programa pelo terminal no diretório do projeto com o comando :
 >λ python server.py run
 
 A Api Restful tem 4 Módulos:
 
 - Alunos.py
 onde tem a classe para criar e listar os alunos
 
 - Provas.py
 Com a classe para criar os gabaritos das provas
 
 - Provas_Alunos.py
 Com as classes para cadastrar as provas dos alunos e listá-las
 
 - Server.py
 Que é o módulo que executa o programa
 
 -----------------------------------------------------------------------------------------------------------------------------------
 
 O caminho do banco de dados precisa estar neste formato no windows. Em Mac e Linux só precisam ser alteradas as barras invertidas por barras simples
 
 ![db](https://user-images.githubusercontent.com/60821255/106252303-e1044500-61f4-11eb-8d3f-b7259434ae30.png)
 
 -----------------------------------------------------------------------------------------------------------------------------------
As funcionalidades do projeto foram testadas com o Insomnia:

Tela do Insomnia com o formato de entrada Json para cadastrar um gabarito
São as alternativas das questões
>"q":["e","d","a","e","c","b","a","a","e","d"]

O peso de cada questão

>"p":[1,2,1,1,2,1,3,1,2,1]

![cprova](https://user-images.githubusercontent.com/60821255/106253489-502e6900-61f6-11eb-893b-2a2eafb4e562.png)

Formato do cadastro das provas dos alunos:
- É passado o id da prova
- O id do Aluno
- E as respostas do aluno

![provas](https://user-images.githubusercontent.com/60821255/106254058-0c882f00-61f7-11eb-9755-c3c78a2d0e33.png)

Buscando a nota dos Alunos pelo ID

![notas](https://user-images.githubusercontent.com/60821255/106254519-8f10ee80-61f7-11eb-81fd-9d3c118427e6.png)

Retornando os Alunos Aprovados com a Média Acima de 7

![apro](https://user-images.githubusercontent.com/60821255/106254750-ddbe8880-61f7-11eb-9823-ea0e9c1594da.png)


E Exibindo todos os alunos da escola


![todos](https://user-images.githubusercontent.com/60821255/106255626-0c892e80-61f9-11eb-9406-ee1b30450229.png)


Buscar as provas de todos os alunos

![tprovas](https://user-images.githubusercontent.com/60821255/106255994-7c97b480-61f9-11eb-935a-273416d6d7c8.png)


Buscar os gabaritos das Provas

![gprovas](https://user-images.githubusercontent.com/60821255/106256255-cb454e80-61f9-11eb-892c-45a8de40f99e.png)


Buscar Aluno por ID

![alunoid](https://user-images.githubusercontent.com/60821255/106256622-46a70000-61fa-11eb-9493-eefd140b9db2.png)


Cadastrando alunos com limite de 100

![alunocr](https://user-images.githubusercontent.com/60821255/106256751-70602700-61fa-11eb-8b6c-c32d8ba57158.png)


E deletando Alunos

![deletaluno](https://user-images.githubusercontent.com/60821255/106256887-a0a7c580-61fa-11eb-9a36-814737bfad15.png)

