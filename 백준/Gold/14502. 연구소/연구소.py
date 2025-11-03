from collections import deque

# 모든 경우의 수
# 벽 세우기
def build_wall(max_row, max_col, depth=0):
    if depth > 2: return
    max_area = 0  # 최대 넓이가 0보다 작을 수 없음

    for i in range(max_row):
        for j in range(max_col):
            if grid[i][j] == 0:
                grid[i][j] = 1
                if (depth == 2):
                    max_area = max(max_area, bfs(max_row, max_col))
                else:
                    max_area = max(max_area, build_wall(max_row, max_col, depth + 1))
                grid[i][j] = 0
    return max_area

# bfs func
def bfs(max_row, max_col):
    q = deque()
    for y, x in virus_coor:  # 바이러스 위치 추가해주기
        q.append((y, x))

    copied = copy(grid)  # 원본의 깊은 복사물
    dxys = [[-1, 0, 1, 0], [0, 1, 0, -1]]  # 상하좌우로 탐색
    visited = [[False for _ in range(max_col)] for _ in range(max_row)]  # bfs 방문 체크

    while q:
        y, x = q.popleft()
        if visited[y][x]: continue
        visited[y][x] = True

        for dy, dx in zip(dxys[0], dxys[1]):
            ny, nx = y + dy, x + dx
            if not ((0 <= ny and ny < max_row and 0 <= nx and nx < max_col) and grid[ny][nx] == 0): continue
            copied[ny][nx] = 1
            q.append((ny, nx))

    # safe area
    area = 0
    for i in range(max_row):
        for j in range(max_col):
            if copied[i][j] == 0: area += 1
    return area

# copy func
def copy(origin):
    ret = []
    for i in range(len(origin)):
        ret.append([])
        for j in range(len(origin[0])):
            ret[i].append(origin[i][j])
    return ret


if __name__ == '__main__':
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 바이러스 위치
    virus_coor = []

    # 바이러스 위치 저장
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                virus_coor.append([i, j])

    ans = build_wall(N, M)
    print(ans)
