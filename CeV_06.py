print("=== TESTANDO TIPOS PRIMITIVOS ===")

a = input("Digite algo: ")
print("O tipo primitivo deste valor é: ", type(a))
print("Só tem espaços?", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanúmero? ", a.isalnum())
print("Está em maiuscúlas? ", a.isupper())
print("Está em maiuscúlas? ", a.islower())
print("Está capitalizada? ", a.istitle())
