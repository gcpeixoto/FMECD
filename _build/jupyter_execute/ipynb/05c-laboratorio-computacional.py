import numpy as np

def banco_de_musicas(n):
    d = {i:'Song #'+str(i) for i in range(1,n+1)}
    return d

def player(n,d,reps):
    player = np.arange(1,n+1)    
    p = lambda x: print(f'@ Mensagem do PLAYER: Você me pediu para tocar {x} músicas.')
    m = []
    for _ in range(reps):        
        mus = d[np.random.choice(player)]        
        print('.... Tocando agora: {}'.format(mus))
        m.append(mus)
    p(reps)
    return m
                            
def tocar(n,r):
    d = banco_de_musicas(n)    
    return player(n,d,r)
              
# musicas tocadas         
mus = tocar(20,10)

print('='*20)
print('Músicas tocadas hoje')
print('='*20)
for m in np.unique(np.sort(np.array(mus))):    
    print(m)