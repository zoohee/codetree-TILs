n, m = map(int, input().split())

one = list(map(int,input().split()))
two = list(map(int,input().split()))
three = list(map(int,input().split()))

for _ in range(m):
    two.insert(0,one.pop())
    three.insert(0,two.pop())
    one.insert(0,three.pop())

print(*one)
print(*two)
print(*three)