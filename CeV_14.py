print("=== DESAFIO 13 ===")

func = float(input("Digite o salário do funcionário: R$ "))
reaj = func + (func * 15) / 100

print("O funcionário que ganhava R$ {:.2f}, terá o aumento para R$ {:.2f}.".format(func, reaj))

print("=== DESAFIO 13 - EXTRA ===")

prod = float(input("Digite o preço do produto: R$ "))

desc = prod - ((prod * 10) / 100)
prazo = prod + ((prod * 15 ) / 100)

print("O produto custa R$ {0:.2f}! \nSe for comprado à vista, tem 10% de desconto, e ficará no valor de R$ {1:.2f}.".format(prod, desc))
print("Mas se for a prazo, ficara R$ {0:.2f}!".format(prazo))