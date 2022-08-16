a, b = map(int,input().split())

def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList
list_a = getMyDivisor(a)
list_a.remove(a)
list_b = getMyDivisor(b)
list_b.remove(b)

if (sum(list_a) == b) and (sum(list_b) == a):
    print('YES')
else:
    print('NO')
