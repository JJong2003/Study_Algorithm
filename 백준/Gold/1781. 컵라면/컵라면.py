import heapq

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)] #데드라인, 컵라면
info.sort()

pq = []
for deadline, ramen in info:
    heapq.heappush(pq, ramen)
    if len(pq) > deadline:
        heapq.heappop(pq)
print(sum(pq))