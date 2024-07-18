n, t = map(int, input().split())
belt = []
belt += list(map(int, input().split()))
belt += list(map(int, input().split()))

def rotate(belt):
    temp = belt[-1]
    for i in range(len(belt)-1, 0, -1):
        belt[i] = belt[i-1]
    belt[0] = temp

for _ in range(t):
    rotate(belt)

for i in range(n):
    print(belt[i], end = " ")
print()
for i in range(n, len(belt)):
    print(belt[i], end = " ")