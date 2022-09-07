N = int(input())
step = [0]
for i in range(N):
    step.append(int(input()))
step = step +[0]
dp = [0]*(N+1)+[0]
dp[1] = step[1]
dp[2] = step[1]+step[2]
for i in range(3,N+1):
    dp[i] = max(dp[i-3]+step[i-1],dp[i-2])+step[i]

print(dp[N])
