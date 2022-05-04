from time import sleep

print("PAR OU IMPAR")

num = int(input("Digite um valor qualquer: "))
print("Um momento que vamos analisar se o número é ímpar ou par...")
print("Processando...")
sleep(2)

if num % 2:
    print("Este número é ímpar")
else: 
    print("Este número é par")