def num(n):
  sum=0
  for i in range(1,n+1,1):
    if n%i==0:
      sum+=1
  return sum

def solution(left, right):
    answer = 0

    for i in range(left,right+1,1):
        if num(i)%2==0:
          answer+=i
        else:
          answer-=i
          
    return answer
