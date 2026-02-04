import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
connected = [list() for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    connected[u].append(v)
    connected[v].append(u)

dp = [[0, 0] for _ in range(N+1)]
def dfs(current, parent):
    # dp[current][0] = 0 있으나마나
    dp[current][1] = people[current-1]
    
    for child in connected[current]:
        if child != parent:
            dfs(child, current)
            dp[current][1] += dp[child][0]
            dp[current][0] += max(dp[child][1], dp[child][0])

dfs(1, -1)
print(max(dp[1]))