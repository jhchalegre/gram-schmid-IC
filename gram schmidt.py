tamanho_vetores = int(input("digite o tamanho do vetor: "))
vetor = []
vetores = []


for i in range(tamanho_vetores):
    vetor = list(map(int, input().split(" ")))
    
    vetores.append(vetor)

def produto_interno(v1, v2) -> float:
    produto = 0
    for i in range(tamanho_vetores):
        produto += v1[i]*v2[i]
    return  produto

def projecao(v1, v2) -> list:
    u1 = []
    for i in range(tamanho_vetores):
        u1.append((produto_interno(v1, v2)/produto_interno(v2, v2))*v2[i])
    return(u1)

def soma(v1,v2) -> list:
    u = []
    for i in range(tamanho_vetores):
        u.append(v1[i] + v2[i])
    return u

def sub(v1, v2) -> list:
    u = []
    for i in range(tamanho_vetores):
        u.append(v1[i] - v2[i])
    return u

def norma(v) -> float:
    acum = 0
    for i in range(len(v)):
        acum += v[i]**2
    return acum**0.5

def vetor_ortonormalizado(v) -> list:
    for i in range(len(v)):
        v[i] = v[i]/norma(v)
    return v

def gram_schmidt(vetores, ortonormalizar=False):
    vetores_ortogonalizados = []
    for i in range(len(vetores)):
        vetor_atual = vetores[i]
        for j in range(i):
            proj = projecao(vetor_atual, vetores_ortogonalizados[j])
            vetor_atual = sub(vetor_atual, proj)
        vetores_ortogonalizados.append(vetor_atual)

    if ortonormalizar:
        vetores_ortogonalizados = [vetor_ortonormalizado(v) for v in vetores_ortogonalizados]

    return vetores_ortogonalizados

print(gram_schmidt(vetores,True))
