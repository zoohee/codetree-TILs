import sys

def check():
    rle = ""
    tmp = a[0]
    cnt = 1
    for i in range(1, len(a)):
        if tmp == a[i]:
            cnt += 1
        else:
            rle += tmp
            rle += str(cnt)
            cnt = 1
            tmp = a[i]
    
    rle += tmp
    rle += str(cnt)
    # print(a, rle)
    return len(rle)

def rotate():
    tmp = a[-1]
    for i in range(len(a)-1, -1, -1):
        a[i] = a[i-1]
    a[0] = tmp


a = list(input())

min_length = sys.maxsize
for i in range(len(a)):
    min_length = min(min_length, check())
    rotate()

print(min_length)