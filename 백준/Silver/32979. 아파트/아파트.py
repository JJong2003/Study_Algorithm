from collections import deque

dq = deque()

N = int(input())
T = int(input())

for i in list(map(int, input().split())):
    dq.append(i)

games = list(map(int, input().split()))
ans = []

for i in range(T):
    g = games[i]
    for j in range(g):
        tmp = dq.popleft()
        if j == g-1:
            ans.append(tmp)
            dq.appendleft(tmp)
            break
        dq.append(tmp)
print(*ans)