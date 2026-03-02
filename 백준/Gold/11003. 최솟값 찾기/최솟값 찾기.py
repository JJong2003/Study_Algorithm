from heapq import heappush, heappop

n, l = map(int, input().split())
A = list(map(int, input().split()))

pq = [(A[0], 0)]

ans = [A[0]]
for i in range(1, n):
    while pq and i-l+1 > pq[0][1]:
        val, idx = heappop(pq)
    heappush(pq, (A[i], i))
    ans.append(pq[0][0])
print(' '.join(map(str, ans)))