from collections import deque

dyxs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def cal_cost(move, corner): return move*100 + corner*500

def solution(board):
    size = len(board)
    # 코너를 어떻게 파악할 것인가?
    inside = lambda x, y : 0<=x<size and 0<=y<size
    
    q = deque([(0, 0, -1, 0, 0)]) # y,x, 진행방향, 코너 개수, 움직인 횟수
    visited = [[[float('inf')]*4 for __ in range(size)] for _ in range(size)]
    visited[0][0][0] = 0
    ans = float('inf')
    while q:
        y, x, dirc, corner, move = q.popleft()
        if y == size-1 and x == size-1: #도착
            ans = min(ans, min(visited[y][x]))
            print(visited[y][x])
            continue
            
        for d in range(4):
            dy, dx = dyxs[d]
            ny, nx = y+dy, x+dx
            if not inside(ny, nx) or board[ny][nx]: continue
            tmp_corner = corner+1 if dirc != -1 and dirc!=d else corner
            
            if cal_cost(move+1, tmp_corner) < visited[ny][nx][d]:
                visited[ny][nx][d] = cal_cost(move+1, tmp_corner)
                q.append([ny, nx, d, tmp_corner, move+1])
    
    return ans