from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
energy = [0]+[int(input()) for i in range(N)]
G = defaultdict(list)
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

# 부모, 거리
st = [[[0, 0] for i in range(N+1)] for j in range(20)]
depth = [0] * (N+1)

# bfs
q = deque([(1, 1)]) #start, deep
depth[1] = 1
while q:
    current, deep = q.popleft()
    for nxt, dist in G[current]:
        if depth[nxt] > 0:
            continue
        st[0][nxt] = [current, dist]
        depth[nxt] = deep+1
        q.append((nxt, deep+1))


for k in range(1, len(st)):
    for i in range(1, N+1):
        _, dist1 = st[k-1][i]
        prev, dist2 = st[k-1][st[k-1][i][0]]

        st[k][i] = [prev, dist1 + dist2]

def sol(ant):
    E = energy[ant]

    for k in range(len(st)-1, -1, -1):
        parent, dist = st[k][ant]
        if dist <= E:
            ant = parent
            E -= dist

    if st[0][ant][1] <= E:
        return st[0][ant][0]
    return ant

for i in range(1, N+1):
    ans = 1 if (k:=sol(i)) == 0 else k
    sys.stdout.write(str(ans)+"\n")
sys.stdout.flush()