def check_beautiful():
    c_2 = b_num.count('2')
    c_3 = b_num.count('3')
    c_4 = b_num.count('4')

    if (c_2 % 2 == 0 and c_3 % 3 == 0 and c_4 % 4 == 0):
        i = 0

        while(i < n):
            check_num = int(b_num[i])
            for j in range(i, i + check_num):
                if(int(b_num[j]) != check_num):
                    return False
            i += check_num

    else:
        return False

    return True


def beautiful_num(num):
    global b_num
    global ans
    if (num == n):
        if (check_beautiful()):
            ans += 1
        return

    for i in range(1, 5):
        b_num += str(i)
        beautiful_num(num + 1)
        b_num = b_num[:-1]

    return


n = int(input())
arr = []
ans = 0
b_num = ''
beautiful_num(0)
print(ans)