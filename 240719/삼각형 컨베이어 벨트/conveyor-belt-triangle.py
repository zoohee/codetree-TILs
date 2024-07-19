n, m = map(int, input().split())

graph = []
for _ in range(3):
    graph += list(map(int, input().split()))

def rotate():
    temp = []
    for i in range(1, m+1):
        temp.append(graph[-i])

    for i in range(len(graph)-1, -1, -1):
        graph[i] = graph[i-m]
    
    for i in range(m-1, -1, -1):
        graph[i] = temp[i-m+1]

rotate()
for i in range(len(graph)):
    if i!= 0 and i % n == 0:
        print()
    print(graph[i], end = " ")