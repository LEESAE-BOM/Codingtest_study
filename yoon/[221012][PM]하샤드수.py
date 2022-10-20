def solution(x):
    s = str(x)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    print(sum, x)
    return not(x % sum)

# def solution(x):return x % sum([n for n in str(x)]) == 0 