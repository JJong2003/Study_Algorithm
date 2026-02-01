from heapq import heappop, heappush

N, K = map(int, input().split())
jewelries = []
for _ in range(N):
    heappush(jewelries, list(map(int, input().split())))

bags = [int(input()) for _ in range(K)]
bags.sort()

ans = 0
tmp_jew = []
for bag in bags:
    while jewelries and bag >= jewelries[0][0]:
        heappush(tmp_jew, -heappop(jewelries)[1])
    if tmp_jew:
        ans += -heappop(tmp_jew)
print(ans)