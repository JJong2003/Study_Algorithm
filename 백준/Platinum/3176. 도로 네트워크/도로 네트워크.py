from collections import defaultdict, deque
import sys
input = sys.stdin.readline

INF = float('inf')

N = int(input())
G = defaultdict(list)
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

# 부모, 최소, 최대
st = [[[0, INF, -INF] for i in range(N+1)] for j in range(20)]
depth = [0] * (N+1)

# bfs
q = deque([(1, 1)]) #start, deep
depth[1] = 1
while q:
    current, deep = q.popleft()
    for nxt, weight in G[current]:
        if depth[nxt] > 0:
            continue
        st[0][nxt] = [current, weight, weight]
        depth[nxt] = deep+1
        q.append((nxt, deep+1))


for k in range(1, len(st)):
    for i in range(1, N+1):
        _, mini1, maxi1 = st[k-1][i]
        prev, mini2, maxi2 = st[k-1][st[k-1][i][0]]

        st[k][i] = [prev, min(mini1, mini2), max(maxi1, maxi2)]


def LCA(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    m, M = INF, -INF
    for i in range(len(st)):
        if diff & (1<<i):
            m = min(m, st[i][a][1])
            M = max(M, st[i][a][2])
            a = st[i][a][0]

    if a == b:
        return m, M

    for i in range(len(st)-1, -1, -1):
        if st[i][a][0] != st[i][b][0]:
            m = min(m, st[i][a][1], st[i][b][1])
            M = max(M, st[i][a][2], st[i][b][2])
            a = st[i][a][0]
            b = st[i][b][0]

    m = min(m, st[0][a][1], st[0][b][1])
    M = max(M, st[0][a][2], st[0][b][2])
    return m, M

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    m, M = LCA(a, b)
    sys.stdout.write(f"{m} {M}\n")
sys.stdout.flush()