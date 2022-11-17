N = int(input())
bolpen = sorted(list(map(int,input().split())),reverse=True)
bolpen2 = sorted(bolpen)
two_pen = 1
three_pen = 1
two_pen2 = 1
three_pen2 = 1
j=0
for i in range(len(bolpen)):
    if bolpen[i]==0:
        continue
    if j==3:
       break
    three_pen*=bolpen[i]
    if j==2:
        three_pen2 *= bolpen2[-1]
    else:
        three_pen2 *= bolpen2[i]
    if j < 2:
        two_pen*=bolpen[i]
        two_pen2*= bolpen2[i]
    j+=1
print(max(two_pen,two_pen2,three_pen,three_pen2))