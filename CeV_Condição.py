print("=== TESTANDO CONDIÇÃO ===")

#nome = str(input("Qual o seu nome?: "))

#if nome == 'Yan':
 #   print("Caramba, que nome foda!")
#else: 
  #  print("Seu nome é fútil!")

#print("Muito prazer em conhecer, {}!".format(nome))

print("CALCULANDO MÉDIA")

n1 = float(input("Digite o valor da primeira nota: "))
n2 = float(input("Digite o valor da segunda nota: "))
m = (n1 + n2) / 2

print("Sua média foi {}".format(m))

if m >= 6:
    print("O aluno foi aprovado!")
else: 
    print("Reprovado!")