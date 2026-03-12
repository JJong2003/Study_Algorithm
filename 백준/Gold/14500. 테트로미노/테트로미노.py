dyxs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for __ in range(N)]
ans = 0


def dfs(y, x, score, depth=1):
    global ans
    if depth == 4:
        ans = max(ans, score)
        return

    for dy, dx in dyxs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            if depth == 2:
                visited[ny][nx] = 1
                dfs(y, x, score + grid[ny][nx], depth + 1)
                visited[ny][nx] = 0
            visited[ny][nx] = 1
            dfs(ny, nx, score + grid[ny][nx], depth + 1)
            visited[ny][nx] = 0
    return


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, grid[i][j])
        visited[i][j] = 0
print(ans)
