print("=== DESAFIO 15 ===")
print("= ALUGUEL DE CARRO =")

km = float(input("Quantos KM você percorreu? "))
dia = int(input("Quantos dias você ficou com o carro? "))

km_vlr = km * 0.15
dia_vlr = dia * 60

print("O valor por {} de KM andado, é de: R$ {}!".format(km, km_vlr))
print("O valor total por ficar {} dias com o carro, é de: R$ {}!".format(dia, dia_vlr))
print("Logo, o valor total é de: R$ {}!".format(km_vlr + dia_vlr))