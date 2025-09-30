def produto_escalar(vetor1, vetor2):
    return  (x1*x2 + y1*y2)

def projecao(vetor1, vetor2):
    return (produto_escalar(vetor1, vetor2))/(produto_escalar(vetor2, vetor2))

def norma (vetor_unico):
    return sqrt(vetor_unico, vetor_unico)
