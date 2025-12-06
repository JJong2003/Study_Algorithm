n = int(input())
electric_wire =  [tuple(map(int, input().split())) for _ in range(n)]
electric_wire.sort(key=lambda x:x[0])

wire_b = [b for a, b in electric_wire]

# LIS
dp = [1] * n
for i in range(n):
    flag = wire_b[i]
    for j in range(i):
        if wire_b[j] < flag:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))