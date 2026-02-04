import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

edges = [list() for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

tree = [list() for _ in range(N+1)]
def makeTree(current, parent):
    for node in edges[current]:
        if node != parent:
            tree[current].append(node)
            makeTree(node, current)

size = [0] * (N+1)
def countSubTreeNodes(current):
    size[current] = 1
    for node in tree[current]:
        countSubTreeNodes(node)
        size[current] += size[node]

makeTree(R, -1)
countSubTreeNodes(R)

for _ in range(Q):
    print(size[int(input())])