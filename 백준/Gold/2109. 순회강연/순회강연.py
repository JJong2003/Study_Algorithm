import heapq

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)] #강연료, 날짜
info.sort(key=lambda x:(x[1]))

pq = []
for p, d in info:
    heapq.heappush(pq, p)
    if len(pq) > d:
        heapq.heappop(pq)
print(sum(pq))