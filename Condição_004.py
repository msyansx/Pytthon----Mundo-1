from time import sleep 
print("CUSTO DA VIAGEM")

print("Vamos calcular sua viagem!!")
viagem = float(input("Qual a distância em KM que você irá viajar?: "))

custo_menor = viagem * 0.5
custo_maior = viagem * 0.45

if viagem <= 200:
    print("O seu custo de viagem é de: R$ {:.2f}".format(custo_menor))
else: 
    print("O seu custo de viagem é de: R$ {:.2f}".format(custo_maior))