import copy
n = int(input())
graph = [[0] * (n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
dp = copy.deepcopy(graph)

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = graph[i][j] + max(dp[i-1][j], dp[i][j-1])

print(dp[n][n])