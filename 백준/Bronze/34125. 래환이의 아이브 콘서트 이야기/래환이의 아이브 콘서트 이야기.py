N, M = map(int, input().split())
grid = [list(input().split()) for _ in range(N)]

cal_dist = lambda y, x : y+1 + abs((M+1)/2 - (x+1))
shrt = float('inf')
ans = [-1]
for i in range(N):
    for j in range(M):
        dist = cal_dist(i, j)
        if grid[i][j] == '0' and dist < shrt:
            shrt = dist
            ans = [i+1, j+1]

print(*ans)