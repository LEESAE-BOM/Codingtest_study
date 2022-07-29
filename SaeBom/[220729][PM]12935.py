def solution(arr):
    answer = []
    if len(arr)<2:
        answer=[-1]
    else:
        arr.remove(min(arr))
        answer=arr
    return answer
