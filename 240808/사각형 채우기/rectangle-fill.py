n = int(input())
# 1 2 3 5 8
dp = [-1]*(1001)
dp[0], dp[1], dp[2] = 0, 1, 2
for i in range(3, n+1):
    dp[n] = dp[n-1] + dp[n-2]

print(dp[n])