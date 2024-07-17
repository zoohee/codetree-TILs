n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
for i in range(n-2):
    for j in range(n-2):
        cnt = 0
        for k in range(i, i+3):
            for l in range(j, j+3):
                if graph[k][l] == 1:
                    cnt += 1
        max_cnt = max(max_cnt, cnt)

print(max_cnt)