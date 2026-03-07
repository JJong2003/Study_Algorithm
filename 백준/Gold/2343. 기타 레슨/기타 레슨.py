n, m = map(int, input().split())
videos = list(map(int, input().split()))

lo, hi = max(videos)-1, sum(videos)+1
while lo+1 < hi:
    x = (lo+hi)//2

    cnt = 1
    length = 0
    for i in range(n):
        v = videos[i]
        if length + v > x:
            cnt += 1
            length = v
        else:
            length += v

    if cnt <= m:
        hi = x
    elif cnt > m:
        lo = x

print(hi)