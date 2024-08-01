n = int(input())
answer = set()

def backtrack(curr, length):
    if length == n:
        answer.add(curr)
        return
    for num in range(1, 5):
        if length + num <= n:
            backtrack(curr+(str(num)*num),length+num)

backtrack("",0)
print(len(answer))