N = int(input())
corn = []
for i in range(5):
    x= list(map(int,list(input())))
    corn.append(x)

def live(corn,i,j):
    sum = 0
    if i-1 >= 0:
        if j-1>=0:
            sum+=corn[i-1][j-1]
        if j>=0:
            sum += corn[i - 1][j]
        if j+1 < 5:
            sum += corn[i - 1][j + 1]
    if i>=0:
        if j-1>=0:
            sum+=corn[i][j-1]
        if j+1 < 5:
            sum += corn[i][j + 1]
    if i+1 < 5:
        if j - 1 >= 0:
            sum += corn[i + 1][j - 1]
        if j >= 0:
            sum += corn[i + 1][j]
        if j + 1 < 5:
            sum += corn[i + 1][j + 1]
    if corn[i][j]==1:
        if sum == 2 or sum ==3:
            return 1
    else:
        if sum == 3:
            return 1
    return 0

def cor(corn):
    life = []
    x = []
    for i in range(5):
        x=[]
        for j in range(5):
            x.append(live(corn,i,j))
        life.append(x)
    return life

for k in range(N):
    corn = cor(corn)

for i in corn:
    for j in i:
        print(j,end='')
    print('')
