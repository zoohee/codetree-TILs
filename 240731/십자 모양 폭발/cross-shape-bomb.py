n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

num = graph[r][c]
for d in range(4):
    for i in range(num):
        if 0 <= r+dx[d]*i < n and 0 <= c+dy[d]*i < n:
            graph[r+dx[d]*i][c+dy[d]*i] = 0

for j in range(n):
    tmp1 = []
    tmp2 = []
    for i in range(n):
        if graph[i][j] == 0:
            tmp2.append(0)
        else:
            tmp1.append(graph[i][j])
    
    for a in range(len(tmp2)):
        graph[a][j] = 0
    for b in range(len(tmp1)):
        graph[b+len(tmp2)][j] = tmp1[b]

for i in range(n):
    print(*graph[i])