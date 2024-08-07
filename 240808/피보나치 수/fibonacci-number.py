n = int(input())

dp = [-1] * 46
def fibbo(n):
    if dp[n] != -1:
        return dp[n]

    if n <= 2:
        return 1
    
    dp[n] = fibbo(n-1) + fibbo(n-2)

    return dp[n]

print(fibbo(n))