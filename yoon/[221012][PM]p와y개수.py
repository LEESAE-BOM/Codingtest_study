def solution(s):
    s = s.lower()
    
    pSum = 0
    ySum = 0
    for idx in range(len(s)):
        if s[idx] == 'p':
            pSum += 1
        elif s[idx] == 'y':
            ySum += 1
    return pSum == ySum