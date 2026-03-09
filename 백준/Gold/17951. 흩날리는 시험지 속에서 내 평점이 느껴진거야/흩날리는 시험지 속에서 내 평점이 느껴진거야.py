N, K = map(int, input().split())
test = list(map(int, input().split()))

lo, hi = 0, 2*10**6 + 1
res = 0
while lo+1 < hi:
    x = (lo + hi) // 2

    cnt = 0
    score = 0
    for i in range(N):
        score += test[i]
        if score >= x:
            cnt += 1
            score = 0

    if cnt == K:
        res = max(res, x)
    if cnt < K:
        hi = x
    else:
        lo = x

print(res)