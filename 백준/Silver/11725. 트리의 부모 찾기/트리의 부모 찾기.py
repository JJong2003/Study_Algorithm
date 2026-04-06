from collections import defaultdict
import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

G = defaultdict(list)
N = int(input())
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a] += [b]
    G[b] += [a]

parent = [0] * (N+1)

def dfs(cur=1, p=0):
    parent[cur] = p
    for nxt in G[cur]:
        if parent[nxt] > 0 or nxt == 1:
            continue
        dfs(nxt, cur)
dfs()
print(*parent[2:],sep='\n')