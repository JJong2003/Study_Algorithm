import heapq, sys
input = sys.stdin.readline

N, M = map(int, input().split())
djs = [i for i in range(N+1)]

def _find(a):
    if djs[a] != a:
        djs[a] = _find(djs[a])
    return djs[a]


def _union(a, b):
    pa, pb = _find(a), _find(b)
    if pa != pb:
        djs[pb] = pa
        return 1
    return 0

info = []
for _ in range(M):
    u, v, w = map(int, input().split())
    heapq.heappush(info, (w, u, v))

weight = []
for i in range(M):
    w, u, v = heapq.heappop(info)
    if _union(u, v):
        weight.append(w)

weight.sort()
print(sum(weight[:-1]))