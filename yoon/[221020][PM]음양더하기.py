def solution(absolutes, signs):
    sum = 0
    for abs, sign in zip(absolutes, signs):
        if sign == True:
            sum += abs
        else:
            sum -= abs
    return sum