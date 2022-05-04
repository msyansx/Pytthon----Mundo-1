from random import choice
print("=== DESAFIO 19 ===")

a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: ")) 
a3 = str(input("Terceiro aluno: "))  
a4 = str(input("Quarto aluno: "))

lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print("O aluno escolhido foi: {}".format(escolhido))

#nome = random.randint(1, 4)

#if (nome == 1):
 #   print ("O sorteado para apagar a lousa foi o Lucas")
#elif (nome == 2):
  #  print ("O sorteado para apagar a lousa foi o Yan")
#elif (nome == 3):
   # print ("O sorteado para apagar a lousa foi o Jean")
#elif (nome == 4):
 #   print ("O sorteado para apagar a lousa foi o Walber")'''
