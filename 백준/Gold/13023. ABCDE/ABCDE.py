from collections import defaultdict
g = defaultdict(list)
n,m=map(int,input().split())
for _ in range(m):
    a,b=map(int,input().split())
    g[a] += [b]
    g[b] += [a]

visited = [0]*(n+1)

def dfs(current, depth=1):
    if depth >= 5:
        return 1
    flag = 0
    for nxt in g[current]:
        if visited[nxt]:
            continue
        visited[nxt] = 1
        flag = max(flag, dfs(nxt, depth+1))
        visited[nxt] = 0
      
    return flag


for i in range(n):
    if not visited[i]:
        visited[i] = 1
        result = dfs(i)
        if result:
            print(1)
            break
        visited[i] = 0
else:
    print(0)