from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
G = defaultdict(list)
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

depth = [0] * (N+1)
sp_tbl = [[[1, 0] for i in range(N + 1)] for j in range(20)] #부모, 거리

q = deque([(1, 1)])
while q:
    cur, deep = q.popleft()
    depth[cur] = deep
    for nxt, dist in G[cur]:
        if depth[nxt] > 0:
            continue
        q.append((nxt, deep+1))
        sp_tbl[0][nxt] = [cur, dist]

for k in range(1, 20):
    for i in range(1, N+1):
        _, dist1 = sp_tbl[k - 1][i]
        p, dist2 = sp_tbl[k - 1][ sp_tbl[k - 1][i][0] ]
        sp_tbl[k][i] = [p, dist1 + dist2]


def LCA(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    dist = 0
    for i in range(len(sp_tbl)):
        if diff & (1<<i):
            dist += sp_tbl[i][a][1]
            a = sp_tbl[i][a][0]
    if a == b:
        return a, dist

    for i in range(len(sp_tbl) - 1, -1, -1):
        if sp_tbl[i][a][0] != sp_tbl[i][b][0]:
            dist += sp_tbl[i][a][1] + sp_tbl[i][b][1]
            a = sp_tbl[i][a][0]
            b = sp_tbl[i][b][0]

    return sp_tbl[0][a][0], dist + sp_tbl[0][a][1] + sp_tbl[0][b][1]

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u, v = query[1:]
        lca, dist = LCA(u, v)
        sys.stdout.write(f"{dist}\n")
    else:
        u, v, k = query[1:]
        lca, dist = LCA(u, v)
        if lca == 0:
            lca = 1

        u_to_lca = depth[u] - depth[lca] + 1

        if k <= u_to_lca:
            target = u
            jump = k - 1
        else:
            target = v
            total_nodes = depth[u] - depth[lca] + 1 + depth[v] - depth[lca]
            jump = total_nodes - k  # v에서 거꾸로 올라가야 하는 횟수

        for i in range(len(sp_tbl)-1, -1, -1):
            if jump & (1<<i):
                target = sp_tbl[i][target][0]

        sys.stdout.write(f"{target}\n")
sys.stdout.flush()
