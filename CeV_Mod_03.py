import math
    
print("=== DESAFIO 18 ===")

n1 = float(input("Digite um grau: "))
#n2 = (n1 * 3.14) / 180
n2 = math.radians(n1)
cosseno = math.cos(n2)
seno = math.sin(n2)
tangente = math.tan(n2)

print("O cosseno de {} é {:.2f}".format(n1, cosseno))
print("O seno de {} é {:.2f}".format(n1, seno))
print("A tangente de {} é {:.2f}".format(n1, tangente))