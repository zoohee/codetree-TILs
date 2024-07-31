n, m = map(int, input().split())
answer = []

def perm(cnt):
    if cnt == m+1:
        for a in answer:
            print(a, end=" ")
        print()
        return
    
    for i in range(1, n+1):
        answer.append(i)
        perm(cnt+1)
        answer.pop()

    return

perm(1)