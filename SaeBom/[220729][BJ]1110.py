def cycle(N):
  org=N
  sum=0
  while(1):
    if N<10:
      a=N
    else:
      a=N//10+N%10
    N=a%10+(N%10)*10
    sum+=1
    if org==int(N):
      print(sum)
      break
      

N = int(input())
cycle(N)
