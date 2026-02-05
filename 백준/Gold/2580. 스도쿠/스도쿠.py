sudoku = [list(map(int, input().split())) for _ in range(9)]

info = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            info.append((i, j))

def makeCandidates(y, x):
    candidates = set(range(1, 10))
    for i in range(9):
        candidates.discard(sudoku[y][i])
        candidates.discard(sudoku[i][x])
    
    ny, nx = 3*(y//3), 3*(x//3)
    for i in range(ny, ny+3):
        for j in range(nx, nx+3):
            candidates.discard(sudoku[i][j])
    return candidates

def solve(idx=0):
    if idx >= len(info):
        for elem in sudoku:
            print(' '.join(map(str, elem)))
        exit(0)
        return
    # y, x 자리에 들어갈 수 있는 후보들을 추림
    y, x = info[idx]
    candidates = makeCandidates(y, x)
    for num in candidates:
        sudoku[y][x] = num
        solve(idx+1)
        sudoku[y][x] = 0

solve()