from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
K = int(input())

pq = []
for i in range(n):
    heappush(pq, (-grid[i][0], i, 0))
    heappush(pq, (-grid[i][m-1], i, m-1))
    if i == 0 or i == n-1:
        for j in range(1, m-1):
            heappush(pq, (-grid[i][j], i, j))

dxys = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [0] * (n*m)
while K > 0:
    val, y, x = heappop(pq)
    if visited[m * y + x]:
        continue
    K -= 1
    sys.stdout.write(str(y+1)+" "+str(x+1)+"\n")
    visited[m * y + x] = 1

    for dy, dx in dxys:
        ny, nx = y+dy, x+dx
        if 0<=ny and ny<n and 0<=nx and nx<m:
            heappush(pq, (-grid[ny][nx], ny, nx))
sys.stdout.flush()