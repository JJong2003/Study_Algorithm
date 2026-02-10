from bisect import bisect_left

n = int(input())
inp_seq = list(map(int, input().split()))

dp = []
pos = [-1] * n
for i in range(n):
    seq = inp_seq[i]
    idx = bisect_left(dp, seq)
    if idx < len(dp):
        dp[idx] = min(dp[idx], seq)
    else:
        if dp and seq == dp[-1]:
            continue
        dp.append(seq)
    pos[i] = idx

length = max(pos)
answer = []
for i in range(n-1, -1, -1):
    if pos[i] == length:
        length -= 1
        answer.append(inp_seq[i])
print(len(answer))
print(*reversed(answer))