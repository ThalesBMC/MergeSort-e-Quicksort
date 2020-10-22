def particao(v, esq, dir):
    pivo = v[esq]; i = esq; j = dir+1
    while(True):
        i+=1
        while v[i] < pivo:
            if i >= dir: break
            i+=1
        j-=1
        while v[j] > pivo:
            if j <= esq: break
            j-=1
        if i >= j : break
        trocar(v,i,j)
    trocar(v,esq,j)
    return j    
def trocar(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp

def quicksort2 (v, esq, dir):
    if esq >= dir: return
    p = particao(v,esq,dir)
    quicksort2(v,esq,p-1)
    quicksort2(v,p+1,dir)
    return v
def quicksort(v, N):
    x=quicksort2(v, 0, N-1)
    print(x)


verdade=True
while verdade==True:
    try:
       folha=input("")
       numero=""
       if "|" in folha:
            separador =folha.split("|")
            for i in range(len(separador)): 
                separador[i] = int(separador[i]) 
            quicksort(separador,tamanho)
       else:
           tamanho=int(folha)
    except EOFError:
        verdade = False