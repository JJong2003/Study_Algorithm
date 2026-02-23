import sys
sys.setrecursionlimit(10**6)

t=int(input())
for _ in range(t):
    n=int(input())
    visitied = [0]*(n+1)
    player = [0]+[int(input()) for i in range(n)]
    def dfs(current, depth=1):
        if current == n:
            return depth
        if visitied[current]:
            return 0
        visitied[current] = 1
        return dfs(player[current], depth+1)
        
    k = dfs(player[1])
    print(k)