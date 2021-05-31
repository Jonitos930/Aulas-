aluno = str(input("Coloca o nome do aluno:"))
nota = float(input("Coloca a nota do aluno:"))
nota2 = float(input("Coloca a 2º nota do aluno:"))
media = (nota + nota2) / 2
if nota < media:
    print("O aluno foi aprovado, a media foi:", media)
if nota > media:
    print("O aluno n foi aprovado , a media foi:", media)