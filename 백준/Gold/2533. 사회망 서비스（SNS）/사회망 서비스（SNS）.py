from collections import defaultdict
import sys
sys.setrecursionlimit(10**6+100)
input = sys.stdin.readline

n = int(input())
G = defaultdict(list)
visited = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dp = [[0, 1] for _ in range(n+1)]

def dfs(current):
    visited[current] = 1
    for nxt in G[current]:
        if visited[nxt]:
            continue
        dfs(nxt)
        dp[current][1] += min(dp[nxt])
        dp[current][0] += dp[nxt][1]

dfs(1)
print(min(dp[1]))