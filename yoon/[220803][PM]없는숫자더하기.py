def solution(numbers):
    answer = 0
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for number in numbers:
        cnt[number] += 1
    for i in range(len(cnt)):
        if(cnt[i] == 0):
            answer += i
    return answer