world=[
    ['R','G','G','R','R'],
    ['R','R','G','R','R'],
    ['R','R','G','R','R'],
    ['R','R','R','R','R'],
]
col = len(world[0])
row = len(world)
pinit = 1./(row*col)
p = [[pinit for x in range(col)]  for y in range(row)]
pHit = 0.7
pMiss = 1- pHit

p_move = 0.8


Measurement = ['G','G','G','G','G']
motion = [[0,0],[0,1],[1,0],[1,0],[0,1]]

# motion, [0,0] no move; [0,1] right; [0,-1] left; [1,0] down; [-1,0] up
def sense(p,Observ):
    q = [[pinit for x in range(col)]  for y in range(row)]
    s = 0
    for i in range(row):
        for j in range(col):
            hit = (Observ == world[i][j])
            q[i][j] =(hit*pHit+(1-hit)*pMiss)*p[i][j]

            s += q[i][j]
#normalization
    for i in range(row):
        for j in range(col):
            q[i][j] /= s
    return q

def move(p,motion):
    q = [[pinit for x in range(col)]  for y in range(row)]
    for i in range(row):
        for j in range(col):
            q[i][j] = p_move*p[(i-motion[0])%len(p)][(j-motion[1])%len(p[i])]+(1-p_move)*p[i][j]
    return q
if(len(Measurement) != len(motion)):
    raise ValueError, "Error of size of Measurement and motion"
else:
    for i in range(len(Measurement)):
        p = move(p,motion[i])
        p = sense(p, Measurement[i])




print(p)