from time import sleep

print("------Carros classicos do João------")
print("|------|" * 4)
print("|Olá tudo bem ?\n|poderia dizer o seu nome?")
sleep(1)
print("|------|" * 4)
nome = str(input("|Coloque o seu nome aqui:"))
print("|------|" * 4)
sleep(1)
print("|Lista de carros:\n|AE86\n|205T16\n|911(930)")
print("|------|" * 4)
print(
    "|O aluguer dos carros todos são o mesmo\n|o valor por dia custa:120 Euros\n|o valor por km custa:0.20cents"
)
kms = float(input("|Quantos quilometros irá percorer?:"))
print("|------|" * 4)
dias = float(input("|Quantos dias irá utilizar o carro?:"))
print("|------|" * 4)
orcamento = (kms * 0.20) + (dias * 120)
print("|O orçamento do seu aluguer vai ser de:", orcamento)
sleep(5)
print("\033c")