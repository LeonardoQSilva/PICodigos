
quantidade = int(input())

soma = 0
cont = 0


while cont < quantidade:
    nota = float(input())
    soma = soma + nota
    cont = cont + 1


media = soma / quantidade
print(media)

