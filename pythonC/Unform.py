p=[]
n=5
for i in range(n):
    p.append(float(1./n))
world=['green','red','red','green','green']

Obsversation=['red','red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
#p=[0,1,0,0,0]
pExact=0.8
pOvershoot=0.1
pUndershoot=0.1

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

def move(p,step):
    q=[]
    for i in range(len(p)):
        q.append((p[i-step]%len(p))*pExact+(p[i-step-1]%len(p))*pUndershoot+(p[i-step]%len(p))*pOvershoot)
    return q

#W = ['red','green']
#print Lsense(p,W)
#for i in range(1000):
#    p=move(p,1)
#print(p)
for i in range(len(Obsversation)):
    p=sense(p,Obsversation[i])
    p=move(p,motions[i])
print p
