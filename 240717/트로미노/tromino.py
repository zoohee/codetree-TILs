n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# ㄴ모양
def one(i, j):
    if i+1 >= n or j+1 >= n:
        return 0
    return graph[i][j]+graph[i+1][j]+graph[i+1][j+1]
    
# ㄴ 뒤집은모양
def two(i, j):
    if i+1 >= n or j-1 < 0:
        return 0
    return graph[i][j]+graph[i+1][j]+graph[i+1][j-1]

# ㄱ 모양
def three(i, j):
    if i+1 >=n or j+1 >= n:
        return 0
    return graph[i][j]+graph[i][j+1]+graph[i+1][j+1]

# ㄱ 뒤집은모양
def four(i, j):
    if i+1 >= n or j-1 < 0:
        return 0
    return graph[i][j]+graph[i][j-1]+graph[i+1][j-1]

# ㅣ 모양
def five(i, j):
    if i+1 >= n or i+2 >= n:
        return 0
    return graph[i][j]+graph[i+1][j]+graph[i+2][j]

# - 모양
def six(i, j):
    if j+1 >= n or j+2 >= n:
        return 0
    return graph[i][j]+graph[i][j+1]+graph[i][j+2]

max_value = 0
for i in range(n):
    for j in range(n):
        max_value = max(max_value, one(i, j), two(i, j), three(i, j), four(i, j), five(i, j), six(i, j))

print(max_value)