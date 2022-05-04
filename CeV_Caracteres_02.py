print("=== DESAFIO 23 ===")

num = int(input("Digite um número: "))

u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
dm = num // 10000 % 10
print("Analisando o número {}".format(num))
print("Milhares: {}".format(dm))
print("Milhar: {}".format(m))
print("Centena: {}".format(c))
print("Dezena: {}".format(d))
print("Unidade: {}".format(u))


