def solution(num):
    if num == 1:
            return 0
    answer = -1
    count = 0
    
    for i in range(500):
        count += 1
        if num%2:
            num = num * 3 + 1
        else:
            num = num / 2
        if num == 1:
            return count
    return answer