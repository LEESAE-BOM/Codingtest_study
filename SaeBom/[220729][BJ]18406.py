def lucky(n):
  left=0
  right=0
  for i in range(int(len(n)//2)):
    left+=int(n[i])
    right+=int(n[i+int(len(n)//2)])
  if left==right:
    print('LUCKY')
  else:
    print('READY')
n = input()

lucky(n)
