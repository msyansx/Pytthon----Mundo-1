print("=== DESAFIO 05 ===")

n1 = int(input("Digite um número: "))

ant = n1 - 1
suc = n1 + 1

print("O sucessor de {} é {}, e o antecesor é {}!".format(n1, suc, ant))
print("=== DESAFIO 06 ===")

n2 = int(input("Digite um valor: "))

dob = n2 * 2
tri = n2 * 3 
r_qd = n2 ** 0.5

#print("O dobro de {} é {} \n O triplo é {}, e  a raiz quadrada é {}!".format(n2, dob, tri, r_qd))
print("""O dobro de {} é {}, o triplo é {}, e a raiz quadrada é {:.2f}!""".format(n2, dob, tri, r_qd))
