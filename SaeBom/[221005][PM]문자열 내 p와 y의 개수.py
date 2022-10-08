def solution(s):
    strp = ['p', 'P']
    stry = ['y', 'Y']
    answer = True

    countp = 0
    county = 0
    for i in s:
        if i in strp:
            countp += 1
        elif i in stry:
            county += 1
    if countp == county:
        return True
    else:
        return False

