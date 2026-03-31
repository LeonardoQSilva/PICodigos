def matriz_borda_crescente( m: int, n: int ) -> list:
    M = list()
    for i in range(m):
        linha = list()
        for j in range(n):  
            linha.append(i + j) 
        M.append(linha) 
    return M 

def matriz_simetrica( m: int, n: int ) -> list:
    M = list()
    for i in range(m):
        linha = list()
        for j in range(n):
            valor = abs(i - j)
            linha.append(valor)
        M.append(linha)
    return M



def eh_matriz_quadrada( M: list ) -> bool:
    num_linhas = len(M)
    if num_linhas == 0:
        return False
    
    num_colunas = len(M[0])
    
    if num_linhas != num_colunas:
        return False
    for linha in M:
        if len(linha) != num_colunas:
            return False
    return True

def eh_diagonal( M: list ) -> bool:
    quadrado = eh_matriz_quadrada(M)
    if quadrado != True:
        return False
    n = len(M)
    for i in range(n):
        for j in range(n):
            if i != j and M[i,j] != 0:
                return false
    return true

def matriz_transposta( M: list ) -> list:
    if not M: return [] 
    
    num_linhas = len(M)
    num_colunas = len(M[0])
    
    T = [] 
    
    for j in range(num_colunas):
        nova_linha = []
        for i in range(num_linhas):
            nova_linha.append(M[i][j])
        T.append(nova_linha)
        
    return T
