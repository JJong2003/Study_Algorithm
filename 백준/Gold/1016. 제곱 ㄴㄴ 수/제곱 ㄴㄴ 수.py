t = 1000050
square = []
for i in range(2, t): #제곱수는
    square.append(i**2)

mini, maxi = map(int, input().split())
board = [1] * (maxi-mini+1)

for s in square: # 제곱수를 기준으로 돌려
    x = ((mini + s - 1) // s ) * s
    x = x // s
    idx = 0
    while mini <= (k:=s*(x+idx)) and k <= maxi:
        board[k-mini] = 0
        idx+=1

print(sum(board))