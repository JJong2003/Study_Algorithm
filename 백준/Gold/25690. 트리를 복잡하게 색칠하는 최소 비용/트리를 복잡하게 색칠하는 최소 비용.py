import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n = int(input())
connected = [list() for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    connected[u].append(v)
    connected[v].append(u)

dp = [list(map(int, input().split())) for _ in range(n)]

def dfs(current, parent):
    for node in connected[current]:
        if node != parent:
            dfs(node, current)
            dp[current][0] += min(dp[node])
            dp[current][1] += dp[node][0]

dfs(0, -1)
print(min(dp[0]))