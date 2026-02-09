C, N = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(reverse=1, key=lambda x: (x[0], (x[0] / x[1])))
dp = [10**6] * (C + 2000)
dp[0] = 0

for i in range(N):
    cost, value = info[i]
    for j in range(value, len(dp)):
        dp[j] = min(dp[j], dp[j-value]+cost)

print(min(dp[C:]))