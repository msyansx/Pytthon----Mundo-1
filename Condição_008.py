print('-=' * 20)
print("ANALISANDO TRIÂNGULO")
print('-=' * 20)

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
v3 = float(input("Digite o terceiro valor: "))

if  v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print("As retas acimas PODEM SER CONSIDERADAS um triângulo.")
else: 
    print("As retas acimas NÃO PODEM SER CONSIDERADAS um triângulo.")