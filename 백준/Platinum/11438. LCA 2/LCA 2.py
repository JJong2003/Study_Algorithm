from collections import defaultdict
import sys
sys.setrecursionlimit(10**6+10)
input = sys.stdin.readline

n = int(input())
G = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    G[u] += [v]
    G[v] += [u]

parent = [[0 for i in range(n+1)] for _ in range(20)]
depth = [-1] * (n+1)

# 그래프 탐색으로 부모 노드, 노드의 깊이 정리
def dfs(current=1, deep=1):
    depth[current] = deep
    for nxt in G[current]:
        if depth[nxt] > 0:
            continue
        parent[0][nxt] = current
        dfs(nxt, deep+1)

dfs()

# 희소 배열
for k in range(1, len(parent)):
    for i in range(1, n+1):
        parent[k][i] = parent[k-1][parent[k-1][i]]


def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    # a의 깊이를 b와 맞춰준다.
    diff = depth[a] - depth[b]
    for i in range(20):
        if diff & (1<<i):
            a = parent[i][a]

    if a == b:
        return a

    for k in range(19, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    p = lca(a, b)
    sys.stdout.write(str(p)+"\n")
sys.stdout.flush()