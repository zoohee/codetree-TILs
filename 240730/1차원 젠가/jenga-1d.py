n = int(input())
arr = [int(input().rstrip()) for _ in range(n)]

for _ in range(2):
    s, e = map(int, input().split())

    tmp = []
    for i in range(len(arr)):
        if s-1 <= i <= e-1:
            continue
        tmp.append(arr[i])
    arr = tmp.copy()

print(len(arr))
for i in range(len(arr)):
    print(arr[i])