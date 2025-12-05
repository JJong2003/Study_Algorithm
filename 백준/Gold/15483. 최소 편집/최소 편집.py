s1 = input()
s2 = input()

dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)] #생성

# 초기화
for i in range(len(dp[0])):
    dp[0][i] = i
for i in range(len(dp)):
    dp[i][0] = i

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        dp[i][j] = min(dp[i][j-1] + 1,
                       dp[i-1][j] + 1,
                       dp[i-1][j-1] + (s1[i-1] != s2[j-1]))

print(dp[len(dp) - 1][len(dp[0]) - 1])