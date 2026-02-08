import sys
input = sys.stdin.readline

N=int(input())
seq = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
for i in range(1,N):
    dp[i][i] = 1
    if seq[i-1] == seq[i]:
        dp[i-1][i] = 1

for length in range(2, N):
    for start in range(N - length):
        end = start + length
        if seq[start] == seq[end] and dp[start+1][end-1]:
            dp[start][end] = 1
    
M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])