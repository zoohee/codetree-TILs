# 0 0 1 1 1 2 2 3 4

n = int(input())
dp = [-1] * 1001
dp[0], dp[1], dp[2], dp[3] = 0, 0, 1, 1

for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-3]

print(dp[n]%10007)