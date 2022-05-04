import math

print("AUMENTOS MÚLTIPLOS")

salario = float(input("Qual o salário do funcionário?: R$ "))

if salario >= 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
  
print("Seu salario com reajuste ficará: R$ {:.2f}".format(novo))