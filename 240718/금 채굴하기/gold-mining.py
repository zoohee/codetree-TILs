# 마름모를 만드는 법은 해당 위치에서 상하좌우 한번더가기
from collections import deque

def bfs(i, j, k):
    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True
    que = deque()
    que.append((i, j, 0))
    cnt = graph[i][j]

    while que:
        x, y, dist = que.popleft()
     
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist <= k:
                cnt += graph[nx][ny]
                visited[nx][ny] = True
                que.append((nx, ny, dist+1))
    
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_cnt = 0
for k in range(n):
    for i in range(n):  
        for j in range(n):
            gold = bfs(i, j, k)
            if k*k+(k+1)*(k+1) <= gold*m:
                max_cnt = max(max_cnt, gold)
                # print(k, gold)
        


print(max_cnt)