from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())

G = defaultdict(list)
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

def dfs(current, dist=0):
    visited[current] = 1
    info = [[dist, current]]
    for nxt, wei in G[current]:
        if visited[nxt]:
            continue
        info.append(dfs(nxt, dist + wei))
    return max(info)

visited = [0] * (N+1)
first = dfs(1)

visited = [0] * (N+1)
second = dfs(first[1])
print(second[0])