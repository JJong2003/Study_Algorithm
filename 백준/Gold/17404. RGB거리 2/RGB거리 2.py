n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')
ans = INF

# 1번째 집을 i 색으로 고정
for i in range(3):
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = [INF, INF, INF]
    dp[0][i] = grid[0][i]

    # 1번 집을 i색으로 고정하면, n번 집은 i색을 사용하면 안 됨
    tmp = grid[n-1][i]
    grid[n-1][i] = INF
    
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + grid[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + grid[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + grid[j][2]
    grid[n-1][i] = tmp

    ans = min(ans, min(dp[n-1]))
print(ans)