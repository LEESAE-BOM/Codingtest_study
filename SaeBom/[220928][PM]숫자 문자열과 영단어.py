character = { 'zero': 0 ,'one':1,'two':2,'three':3,
             'four':4,'five':5,'six':6
            ,'seven':7,'eight':8,'nine':9}
x = ['0','1','2','3','4','5','6','7','8','9']
def solution(s):
    answer = ""
    temp=""
    for i in range(len(s)):
        if s[i] in x:
            answer+=s[i]
        else:
            temp+=s[i]
            if temp in character:
                answer+=str(character[temp])
                temp=""
    answer=int(answer)
    return answer  