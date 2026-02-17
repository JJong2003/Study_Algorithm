n = int(input())
P = list(map(int, input().split()))
visited = [0]*n

def dfs(current):
    visited[current] = 1
    nxt = P[current]
    if visited[nxt]:
        return 1
    return dfs(nxt)

loop = 0
for i in range(n):
    if not visited[i]:
        loop += dfs(i)
print((loop>1)*loop)