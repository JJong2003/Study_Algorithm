import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N,M = map(int, input().split())

graph = {i:[] for i in range(1,N+1)}
indegree = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u] += [v]
    indegree[v] += 1

pq = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heappush(pq, i)

answer = []
while pq:
    num = heappop(pq)
    answer.append(str(num))
    for i in graph[num]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heappush(pq, i)

print(' '.join(answer))