from time import sleep 
aluno = str(input("Coloca o nome do aluno:"))
nota = float(input("Coloca a nota do aluno:"))
nota2 = float(input("Coloca a 2º nota do aluno:"))
(nota + nota2) / 2
media=10 
if media < (nota + nota2) / 2 :
    print("O aluno:",aluno, "foi aprovado, a media foi:", (nota + nota2) / 2)
    sleep(5)
    print("\033c")
else:
    print("O aluno n foi aprovado , a media foi:", (nota + nota2) / 2)
    print("Irá ter que estudar mais!!!",aluno)
    sleep(5)
    print("\033c")