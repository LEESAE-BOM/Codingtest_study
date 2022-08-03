def solution(left, right):
    numbers = list(range(left,right + 1,1))
    answer = 0

    for i in range(len(numbers)):
        count = 0
        n = numbers[i]
        
        for j in range(1, n+1):
            print(n, j)

            if n%j == 0 or j == 1:
                count+=1

        if count%2:
            answer-=n
        else:
            answer+=n
            
    return answer