n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 행부터 검사

answer = 0
for i in range(n):
    for j in range(n-m+1):
        check = False
        for k in range(m):
            if graph[i][j] != graph[i][j+k]:
                check = True
                break

        if not check:
            answer += 1
            break

for i in range(n):
    for j in range(n-m+1):
        check = False
        for k in range(m):
            if graph[j][i] != graph[j+k][i]:
                check = True
                break

        if not check:
            answer += 1
            break

print(answer)