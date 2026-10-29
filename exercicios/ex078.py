lista = []
continuar = 's'
digitados = 0
while True:
    if continuar == 's':
        num = int(input("Digite un valor"))
        lista.append(num)
        digitados += 1
        continuar = str(input("Quer continuar?")).strip().lower()[0]
    else:
        break
lista.sort(reverse=True)
print('Foram digitados (digitadas) números')
print('A ordes decrescente dos valores digitados (lista)')
if 5 in lista:
    print('valor 5 foi digitado')
else:
    print('valor 5 não foi digitado')
