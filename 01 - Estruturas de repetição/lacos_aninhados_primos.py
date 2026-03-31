n1 = int(input())
n2 = int(input())
limite_saida = int(input())
linhas_impressas = 0

for i in range(1, n1 + 1):
    if linhas_impressas >= limite_saida:
        break
    for j in range(n2, 0, -1):
        soma = i + j
        
        # saber se é primo
        divisores = 0
        for k in range(1, soma + 1):
            if soma % k == 0:
                divisores += 1
        
        if divisores == 2: #pulando se for primo
            continue
            
        print(i, j)
        linhas_impressas += 1
        
        if linhas_impressas >= limite_saida:
            break

if linhas_impressas < limite_saida:
    print(limite_saida - linhas_impressas)