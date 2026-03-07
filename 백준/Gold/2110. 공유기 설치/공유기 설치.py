N, M = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

lo, hi = 0, home[-1] - home[0] + 1
while lo+1 < hi:
    x = (lo+hi)//2

    router = 1
    current = home[0]
    for i in range(1, N):
        dist = home[i] - current
        if dist > x:
            router += 1
            current = home[i]
    
    if router < M:
        hi = x
    else:
        lo = x
print(hi)