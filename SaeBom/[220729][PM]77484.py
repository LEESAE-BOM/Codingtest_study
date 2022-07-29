def solution(lottos, win_nums):
    #answer = []
    k=0
    x=lottos.count(0)
    for i in lottos:
      if i in win_nums:
        k+=1
    # k는 일치하는 번호 개수 , x는 0 개수
    if (k==0)&(x==0):
        return [6,6]
    elif k==0:
        return [1,6]
    else:
        answer=[7-(k+x),7-(k)]
    return answer
