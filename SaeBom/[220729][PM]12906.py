def solution(arr):
    answer = []
    
    counter=0
    print(1)
    for i in range(0,len(arr),1):
        if arr[i] not in answer:
            answer.append(arr[i])
            counter=0
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer
