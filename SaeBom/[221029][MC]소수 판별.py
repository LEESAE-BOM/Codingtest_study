import math


def isPrime2(n):
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n == 1:
        return 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return 0
    return 1
n = int(input())
print(isPrime2(n))