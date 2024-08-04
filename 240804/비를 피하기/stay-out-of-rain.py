# 0:이동가능 1:벽(이동불가) 2:사람이서있음 3:비를피하는공간
from collections import deque

def bfs(x, y):
    que = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    while que:
        x, y, dist = que.popleft()
        if graph[x][y] == 3:
            return dist

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 1:
                que.append((nx, ny, dist+1))
                visited[nx][ny] = True
    
    return -1


n, h, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = [[0] * n for _ in range(n)]
people_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            answer[i][j] = bfs(i, j)
            people_cnt += 1
        
        if people_cnt == h:
            for row in answer:
                print(*row)
            exit(0)