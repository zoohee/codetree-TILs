import copy
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = copy.deepcopy(graph)

for i in range(1, n):
    for j in range(n-1):
        for k in range(i):
            dp[i][j] = max(dp[i][j], dp[i][j]+dp[i-1][k])

print(max(dp[n-1]))