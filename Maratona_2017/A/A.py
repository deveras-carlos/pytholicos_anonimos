#APOS UM MÊS RETORNAMOS MAIS FORTES _> Daqui a um mês eu termino, eu prometo

N, Q = map( int, input().split() )

V = [ 1 for _ in range( N ) ]

S = [0 for _ in range(4*N)]
lazy = [0 for i in range(4*N)]

freqs = { 1 : n for n in range( N ) }

print(S)

ELEMENTO_NEUTRO = [[],[]]

#Build
def freq(l, r):

    chaves_l = set(l[0])
    chaves_r = set(r[0])

    intersec = chaves_l & chaves_r

    resposta = [[], []]

    for k in intersec:
        i_l= l[0].index(k)
        i_r = r[0].index(k)
        resposta[0].append(k)
        resposta[1].append(l[1][i_l]+r[1][i_r])
    
    for k in chaves_r - intersec:
        i_r= r[0].index(k)
        resposta[0].append(k)
        resposta[1].append(r[1][i_r])
    
    for k in chaves_l - intersec:
        i_l= l[0].index(k)
        resposta[0].append(k)
        resposta[1].append(l[1][i_l])

    
    return resposta
    

def build(p: int, l: int, r: int):

    if l == r:
        S[p] = [[V[l]], [1]]
        return S[p]
    
    m = (l+r)//2
    
    freq_set = freq(build(2*p, l, m), build(2*p+1, m+1, r))
    S[p] = freq_set 
    return S[p]


def query(a: int, b:int, p:int, l:int, r:int):

    if lazy[p] != 0:
        tam = len(S[p][0])
        for i in range(tam):
            S[p][0][i] += lazy[p]

        lazy[p] = 0

    if b < l or a > r:
        return ELEMENTO_NEUTRO
    
    if a <= l and r <= b:
        return S[p]
    
    m = (l+r)//2
    freq_set = freq(query(a, b, 2*p, l, m), query(a, b, 2*p+1, m+1, r))
    S[p] = freq_set 
    return S[p]

    
def update(a: int, b:int,  v: int, p: int, l: int, r: int):
 
    if lazy[p] != 0:
        tam = len(S[p][0])
        for i in range(tam):
            S[p][0][i] += lazy[p]
        lazy[p] = 0

    if a > r or b < l:
        return S[p]
    
    if l >= a and r <= b:
        tam = len(S[p][0])
        for i in range(tam):
            S[p][0][i] += v

        lazy[2*p] += v
        lazy[2*p+1] += v
        return S[p]
    
    m = (l+r)//2

    freq_set = freq(update(a, b, v, 2*p, l, m), update(a, b, v, 2*p+1, m+1, r))
    S[p] = freq_set 
    return S[p]

build(1, 0, N-1)

for _ in range( Q ):
    a, b = map( int, input().split())
    print(S)
    ans = query(a, b, 1, 0, N-1)
    max_freq = max(ans[1])
    idx = ans[1].index(max_freq)
    frecx = ans[0][idx]
    update(a, b, frecx, 1, 0, N-1)
    print(S)


def visita_folhas(p:int, l:int , r:int):
    pass






















    


