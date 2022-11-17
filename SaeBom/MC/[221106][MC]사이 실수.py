A,B = map(float,input().split())
A=round(A*100)
B=round(B*100)
k=0
while(1):
    if int(A)==int(round(B)):
        print('%.2f' % (A / 100))
        break
    print('%.2f' % (A/100),end=' ')
    A=A+1
    k+=1
