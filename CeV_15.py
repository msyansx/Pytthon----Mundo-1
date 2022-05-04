print("=== DESAFIO 14 ===")
print("CONVERTENDO CELSIUS -> FARENHEIT\n")

var1 = float(input("Digite um valor para Graus Celsius: "))
fah = (var1 * 1.8) + 32

print("A temperatura de {0} graus Celsius, convertido em Farenheit é: {1}!".format(var1, fah))
print("\nCONVERTENDO FARENHEIT -> CELSIUS ")

var2 = float(input("Digite um valor para Graus Farenheit: "))
cel = (var2 - 32) / 1.8
print("A temperatura de {0} graus Farenheit, convertido em Celsius é: {1:.2f}!".format(var2, cel))