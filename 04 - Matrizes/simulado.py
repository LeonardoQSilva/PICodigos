def eh_matriz(M):
    if not M:
        return False
    largura_referencia = len(M[0])
    for linha in M:
        if len(linha) != largura_referencia:
            return False
    return True



def busca_letra(M, item):
    R = list()

    #percorrer cada linha 
    for i in range(len(M)):
        #percorrer cada coluna de cada linha
        for j in range(len(M[i])):
            if M[i][j] == item:
                R.append([i, j])
    return R

def verifica_palavra(M:list, i:int, j:int, palavra: str, direcao_i:int, direcao_j:  int): # recebeu a matriz com as letras,linha que a primeira letra que será verificada está, coluna que a primeira letra verificada está, direção vertical da proxima letra, direção horizontal da proxima letra
    if len(palavra) == 0: #se a palavra acabar pronto conseguimos achar
        return True
    if i < 0 or i >= len(M) or j < 0 or j >= len(M[0]): #se a letra inicial estiver fora da matriz tambem retornamos falso impossivel achar a palavra
        return False
    if M[i][j] != palavra[0]: #retorna falso se a letra analisada for diferente da primeira letra da palavra
        return False
    proxima_linha = i + direcao_i #avança para a proxima linha
    proxima_coluna = j + direcao_j #avança para a proxima coluna
    resto_da_palavra = palavra[1:] #primeira letra confirmada vamos tentar achar a proxima na direção que queremos
    return verifica_palavra(M, proxima_linha, proxima_coluna, resto_da_palavra, direcao_i, direcao_j) #chamou a função denovo buscando a proxima letra, se nao tiver a proxima na direção pedida a função ja da false e termina


def caca_palavra(M, palavra):
    posicoes_iniciais = busca_letra(M, palavra[0]) # roda o busca letra pra achar na matriz todos os lugares que contem a primeira letra da palavra
    direcoes = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]] #salva todas as direções possiveis para facilitar
    for pos in posicoes_iniciais: #analisa uma por uma das posicoes iniciais
        linha_ini, coluna_ini = pos[0], pos[1]  #atribui o i e o j da verifica palavra as coordenadas da posição da primeira letra achada
        for d in direcoes: # analisa cada direção das opções
            dir_i, dir_j = d[0], d[1] # atribui o i e o j de cada direção para colocar na função verifica palavra

            if verifica_palavra(M, linha_ini, coluna_ini, palavra, dir_i, dir_j): # finalmente vai testando cada posição inicial achada com a função busca letra em todas as direções ate achar a palavra e no fim retorna a posição da primeira letra e a direção que a palavra segue
                return [pos,d]
    return None # retorna none se nao acha em lugar nenhum





