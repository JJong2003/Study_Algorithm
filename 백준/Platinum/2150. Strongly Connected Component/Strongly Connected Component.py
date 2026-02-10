import sys
sys.setrecursionlimit(10**5)

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    G[a] += [b]

visited_order = [0] * (V+1) #방문순서
low = [0] * (V+1) #사이클
seq = 0
stack = []
answers = []

def scc(current):
    global seq
    seq += 1
    visited_order[current] = low[current] = seq

    stack.append(current)

    for adj in G[current]:
        if visited_order[adj] == 0:
            scc(adj)
            low[current] = min(low[current], low[adj])
        elif visited_order[adj] < visited_order[current] and adj in stack:
            low[current] = min(low[current], visited_order[adj])

    if visited_order[current] == low[current]:
        tmp = stack.pop()
        answers.append([tmp])
        while stack and tmp != current:
            tmp = stack.pop()
            answers[-1].append(tmp)
        answers[-1].sort()

for i in range(1, V+1):
    if visited_order[i] == 0:
        scc(i)

print(len(answers))
answers.sort()
for elem in answers:
    print(*elem,'-1')