import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            home.append((i, j))
        elif grid[i][j] == 2:
            chicken.append((i, j))

select = set()
ans = float('inf')

# 모든 집들과 거리를 구함
def get_city_dist(s):
    city = 0
    for h in home:
        local = 10000
        for sel in s:
            local = min(local, abs(h[0] - sel[0]) + abs(h[1] - sel[1]))
        city += local
    return city

def btk(idx=0):
    global ans
    
    if len(select) >= M:
        return get_city_dist(select)

    for i in range(idx, len(chicken)):
        ch = chicken[i]
        if ch in select:
            continue
        select.add(ch)
        ans = min(ans, btk(i+1))
        select.discard(ch)

    return ans

print(btk())