def distancia_edicao(a, b):
    m = len(a)
    n = len(b)

    custo = [[0] * (n + 1) for _ in range(m + 1)]
    print("CUSTO",custo)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                custo[i][j] = j  
            elif j == 0:
                custo[i][j] = i  
            elif a[i - 1] == b[j - 1]:
                custo[i][j] = custo[i - 1][j - 1] 
            else:
                custo[i][j] = 1 + min(custo[i - 1][j],      
                                      custo[i][j - 1],      
                                      custo[i - 1][j - 1])  

    return custo[m][n]

a1 = "asar"
b1 = "casa"
print(distancia_edicao(a1, b1))  # Saída: 2

a2 = "inserir"
b2 = "inserção"
print(distancia_edicao(a2, b2))  # Saída: 3

print(distancia_edicao("Jinnison","livia"))