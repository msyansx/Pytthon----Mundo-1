#print("=== DESAFIO 12 A ===")

#prod = float(input("Digite o preço do produto: R$"))
#desc = prod - ((prod * 5) / 100) 
#desc = prod * 0.95 
#desc = (prod * 95 ) / 100

#print("O valor do produto com desconto é R$ {}".format(desc))

print("=== DESAFIO 12 B ===")

prod = float(input("Digite o preço do produto: R$"))
vlr_desc = float(input("Quanto porcentos de desconto você quer? "))

if(vlr_desc > 70):
    print("Não podemos aplicar este valor de desconto!")
else:
    desc = prod - ((prod * vlr_desc  / 100))

    print("O valor do produto com desconto é R$ {}".format(desc))