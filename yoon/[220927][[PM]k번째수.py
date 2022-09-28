def solution(array, commands):
    answer = []
    
    for i in range(len(commands)) :
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        
        sorted_answer= sorted(array[a-1:b])
        answer.append(sorted_answer[c-1])
    
    return answer