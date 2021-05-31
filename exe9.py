print("|=====|"*6)
from time import sleep 
dinheiro=float(input("|Coloque aqui o seu dinheiro em euros:"))
print("|=====|"*6)
reais=(dinheiro*6.34)
print("O seu dinheiro em reais é:",reais)
print("|=====|"*6)
sleep(5)
print("\033c") 