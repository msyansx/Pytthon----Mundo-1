print("=== DESAFIO 10 ===")
print("Conversão pra dólar")

real = float(input("Digite a quantidade de reais que você possui: R$ "))
dol = 3.27

dólar = real / dol
#print("Com R$ {}, você consegue comprar U$ {:.2f}!".format(real, dólar))
print("Você tem R$ {0}. \nCom R$ {0} você pode comprar U$ {1:.2f}!".format(real, dólar))

