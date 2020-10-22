def merge(v, esq, meio, dir):
    i = esq
    j = meio + 1
    for k in range(esq,dir+1): aux[k] = v[k]
    for k in range(esq,dir+1):
        if i > meio: v[k] = aux[j]; j+=1
        elif j > dir: v[k] = aux[i]; i+=1
        elif aux[i] > aux[j]: v[k] = aux[j]; j+=1
        else: v[k] = aux[i]; i+=1

def mergesort2 (v, esq, dir):
    if esq >= dir: return
    meio = (esq + dir)//2
    mergesort2(v,esq,meio)
    mergesort2(v,meio+1,dir)
    merge(v,esq,meio,dir)
    return v
def mergesort (v, N):
    global aux
    aux = list(v)
    x=mergesort2(v,0,N-1)
    print(x)
    del aux

verdade=True
while verdade==True:
    try:
       folha=input("")
       numero=""
       if "|" in folha:
            separador =folha.split("|")
            for i in range(len(separador)): 
                separador[i] = int(separador[i]) 
            mergesort(separador,tamanho)
       else:
           tamanho=int(folha)
    except EOFError:
        verdade = False

