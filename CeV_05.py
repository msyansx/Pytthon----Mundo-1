print ("=== DESAFIO 04 ===")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
s = a + b
m = a * b
d = a / b
di = a // b 
ex = a ** b


print("A soma é {}, o produto é {}, a divisão é {}" .format(s, m, d), end=' ')
print("a divisão inteira é {}, a potência é {}!".format(di, ex))
