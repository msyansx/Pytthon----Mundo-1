print("=== DESAFIO 26 ===")

nome = (input("Digite seu nome completo: ")).strip().upper()

print("A letra 'A' aparece {} vezes.".format(nome.count('A')))
print("A posição da letra 'A' começa na {} posição.".format(nome.find('A')+1))
print("A última letra 'A' aparece na {} posição.".format(nome.rfind('A')+1))