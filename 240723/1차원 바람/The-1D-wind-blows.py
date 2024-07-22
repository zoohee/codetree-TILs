n, m, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
r, d = input().split()
r = int(r) - 1


def rotate(row, direction):
    if direction == 'L':
        tmp = graph[row][-1]
        for i in range(m-1, 0, -1):
            graph[row][i] = graph[row][i-1]
        graph[row][0] = tmp
    elif direction == 'R':
        tmp = graph[row][0]
        for i in range(m-1):
            graph[row][i] = graph[row][i+1]
        graph[row][-1] = tmp

def infection(row, direction):
    if direction == 'U':
        if row - 1 >= 0:
            for i in range(m):
                if graph[row][i] == graph[row-1][i]:
                    return True
    elif direction == 'D':
        if row + 1 < n:
            for i in range(m):
                if graph[row][i] == graph[row+1][i]:
                    return True

    return False


rotate(r, d)

next_d = 'R' if d=='L' else 'L'
direction = 'U'
for i in range(r, 0, -1):
    if infection(i, direction):
        rotate(i-1, next_d)
        next_d = 'R' if next_d=='L' else 'L'
    else:
        break

next_d = 'R' if d=='L' else 'L'
direction = 'D'
for i in range(r, n):
    if infection(i, direction):
        rotate(i+1, next_d)
        next_d = 'R' if next_d=='L' else 'L'
    else:
        break

for i in range(n):
    print(*graph[i])