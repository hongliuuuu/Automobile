p=[]
n=5
for i in range(n):
    p.append(float(1./n))
world=['green','red','red','green','green']
Obsversation='red'
pHit = 0.6
pMiss = 0.2

def sense(p, w):
    q=[]
    for i in range(len(p)):
        hit = (w ==world[i] )
        q.append((hit*pHit+(1-hit)*pMiss)*p[i])
    s=sum(q)
    for i in range(len(q)):
        q[i]/=s
    return q
def Lsense(p,W):
    for i in range(len(W)):
        p = sense(p,W[i])
    return p
W = ['red','green']
print Lsense(p,W)


