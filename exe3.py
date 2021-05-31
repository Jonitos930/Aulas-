from time import sleep

funcionario = str(input("Coloque o nome do funcionario:"))
print("")
salario = float(input("Coloque o salario do funcionario:"))
print("")
print("O salario do:", funcionario, "\nE o seu salario foi de:", salario,
      "no mes de junho.")

sleep(5)
print("\033c")