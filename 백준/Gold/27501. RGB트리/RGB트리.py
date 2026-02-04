import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N = int(input())
connected = [list() for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    connected[u].append(v)
    connected[v].append(u)

rgb = ['R', 'G', 'B']   

color = [[0, 0, 0]]
for _ in range(N):
    color.append(list(map(int, input().split())))

def dfs(current, parent):
    for node in connected[current]:
        if node == parent:
            continue
        dfs(node, current)
        for i in range(3):
            if color[node][(i+1)%3] > color[node][(i+2)%3]:
                color[current][i] += color[node][(i+1)%3]
            else:
                color[current][i] += color[node][(i+2)%3]
dfs(1, -1)

color_path = [0] * (N+1)
def find_path(current, parent, color_num):
    color_path[current] = color_num
    
    for node in connected[current]:
        if node == parent:
            continue
        if color[node][(color_num+1)%3] > color[node][(color_num+2)%3]:
            find_path(node, current, (color_num+1)%3)
        else:
            find_path(node, current, (color_num+2)%3)
ans = max(color[1])
find_path(1, -1, color[1].index(ans))
print(ans)
for i in range(1, N+1):
    print(rgb[color_path[i]], end='')
    