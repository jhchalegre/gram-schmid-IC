tamanho_vetores = int(input("digite o tamanho do vetor: "))
vetor = []
vetores = []

for i in range(tamanho_vetores):
    vetor = list(map(int, input().split(" ")))
    
    vetores.append(vetor)

def produto_interno(vetor1, vetor2):
    return  (vetor1[0]*vetor2[0] + vetor1[1]*vetor2[1])

def projecao(v1, v2):
    for i in range(tamanho_vetores):
        v2[i] = (produto_interno(v1, v2)/produto_interno(v2, v2))*v2[i]
    return(v2)

def norma (v):
    acum = 0
    for i in range(len(v)):
        acum += v[i]**2
    return acum**0.5

print(projecao(vetores[0], vetores[1]))
