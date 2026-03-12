from collections import deque

N, K = map(int, input().split())
q = deque([(N, 0)])

visited = [0] * 200001
shortest = float('inf')
cnt = 0
while q:
    now, time = q.popleft()
    visited[now] = 1
    if shortest < time:
        continue

    if now == K:
        if shortest > time:
            shortest = time
            cnt = 1
        elif shortest == time:
            cnt += 1
        continue

    for nxt in [now-1, now+1, now*2]:
        if nxt < 0 or nxt > 200000 or visited[nxt]:
            continue
        q.append((nxt, time+1))
print(shortest)
print(cnt)