def solution(s):
    answer = ''
    if len(s) % 2 != 0 :
        idx = int(len(s) / 2)
        answer = s[idx]
    
    else :
        idx = int(len(s)/2)
        answer = s[idx-1:idx+1]
        
    return answer