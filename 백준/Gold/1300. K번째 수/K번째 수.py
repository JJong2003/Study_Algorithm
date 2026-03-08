N = int(input())
K = int(input())

lo, hi = 0, K+1
while lo+1 < hi:
    x = (lo+hi)//2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(x//i, N)

    if cnt >= K:
        hi = x
    else:
        lo = x
print(hi)