from time import sleep 

print("~=" * 20)
print("EXERCÍCIO 36")
print("~=" * 20)

casa_vlr = float(input("Qual é o valor da casa? R$ "))
sal_vlr = float(input("Qual o seu salário atual? R$"))
anos_pgto = int(input("E em quantos anos você pretende pagar? "))

# Convertendo anos para meses
meses = anos_pgto * 12

# Calculando o valor da prestação mensal
prestacao = (casa_vlr / meses)

print("Processando...")
sleep(3)
print("Valor da prestação {:.2f}".format(prestacao))

if prestacao > (sal_vlr * 30) / 100:
    print("Empréstimo negado.")

elif prestacao <= 0:
    print("Valor incorreto, por favor refaça com números válidos.")
else: 
    print("Parabéns, empréstimo aprovado!")

print("O valor de 30% do salário é de: R$ {}".format(sal_vlr * 30 / 100))

