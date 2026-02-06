n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

parent = [i for i in range(n*m)]
cnt_node = [1 for i in range(n*m)]

def _find(x):
    if x != parent[x]:
        parent[x] = _find(parent[x])
    return parent[x]

def _union(a, b):
    pa = _find(a)
    pb = _find(b)

    if pa == pb:
        return
    if cnt_node[pa] < cnt_node[pb]:
        pa, pb = pb, pa
    parent[pb] = pa
    cnt_node[pa] += cnt_node[pb]


dyxs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
inside = lambda y,x : 0<=y<n and 0<=x<m
for i in range(n):
    for j in range(m):
        if grid[i][j] == '0':
            for dy, dx in dyxs:
                ny, nx = i+dy, j+dx
                if not inside(ny, nx) or grid[ny][nx] == '1':
                    continue
                _union(m*i+j, m*ny+nx)

answer = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':
            answer[i][j] = 1
            move = set()
            for dy, dx in dyxs:
                ny, nx = i + dy, j + dx
                if inside(ny, nx):
                    comp_root = _find(m*ny+nx)
                    if comp_root in move or grid[ny][nx] == '1':
                        continue
                    move.add(comp_root)
                    answer[i][j] += cnt_node[comp_root]
            answer[i][j] %= 10
            
for elem in answer:
    print(''.join(map(str, elem)))
    