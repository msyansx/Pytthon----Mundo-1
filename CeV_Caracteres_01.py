print("=== DESAFIO 22 ===")

frase = str(input("Digite o nome completo: ").strip())

maius = frase.upper()
minus = frase.lower()
total_letra = len(frase)-frase.count(' ')
pri_nome = frase.find(' ')

print("Em maiúsculo fica: {}".format(maius))
print("Em minúsculo fica: {}".format(minus))
print("Tem um total de {} caractéres.".format(total_letra))
#print("O primeiro nome tem o total de {} caractéres.".format(pri_nome))
separa = frase.split()

print("Seu primeiro nome é {}, e tem {} letras".format(separa[0], len(separa[0])))
