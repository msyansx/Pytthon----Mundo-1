print("=== DESAFIO 09 ===")

v1 = int(input("Digite um valor: "))
tab = 0

print('=' * 18)
print("Tabuada do {}".format(v1))
print('=' * 18)

while(tab <= 20):
    print('{} x {} = {}'.format(v1, tab, (v1 * tab)))
    tab += 1