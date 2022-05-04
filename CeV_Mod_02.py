import math
print("=== DESAFIO 17 ===")

co = float(input("Digite um valor para ao cateto oposto: "))
ca = float(input("Digite um valor para o cateto adjascente: "))

hip = math.hypot(co, ca)
print("O valor da hipotenusa é {:.2f}!".format(hip))