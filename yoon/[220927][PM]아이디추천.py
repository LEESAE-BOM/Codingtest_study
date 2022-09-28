def solution(new_id):
    answer = ''

    newid = new_id.lower()
    
    newid=newid.replace("^","").replace("=","").replace("+","-").replace('!','')
    newid=newid.replace('@','').replace('#','').replace('*','')
    newid=newid.strip('.')
    
    newid=newid.replace('...','.').replace('..','.')
    answer=newid[:15]

    if answer and answer[0] == ".":
        answer=answer[1:]
    if answer and answer[-1] =="." :
        answer=answer[:-1]

    if answer =='': answer='aaa'
    return answer
