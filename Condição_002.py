print("RADAR ELETRÔNICO")

print("Atenção, radar de velocidade!")
veloc = int(input("Digite sua velocidade: "))

if veloc > 80:
    print("Você foi multado!")
    multa = (veloc - 80) * 7
    print("O valor total da multa é de: R$ {}".format(multa))
else: 
    print("Você está dentro do limite de velocidade") 


    