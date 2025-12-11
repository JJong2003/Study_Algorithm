N = int(input())
matrix = []
for i in range(N-1):
    a, b = map(int, input().split())
    matrix.append(a)
a, b = map(int, input().split())
matrix += [a, b]

# dp 초기화
INF = float('inf')
dp = [[INF for _ in range(N+1)] for __ in range(N+1)]
for i in range(N):
    dp[i+1][i+1] = 0

for L in range(1, N):
    for i in range(1, N-L +1):
        j = i + L
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i-1] * matrix[k] * matrix[j])

print(dp[1][N])