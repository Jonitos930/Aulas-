from time import sleep

funcionario = str(input("Coloque o nome do funcionario:"))
print("")
salario = float(input("Coloque o salario do funcionario:"))
print("")
conta = salario * 1.15
print("O salario do:", funcionario, "\nE o seu salario foi de:", salario,
      "no mes de junho.")
print("Mas para o proximo mes o funcionario;", funcionario, "\nirá receber",
      conta)

sleep(5)
print("\033c")