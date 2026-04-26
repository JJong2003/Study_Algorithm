from collections import deque

q = deque()

n, l = map(int, input().split())
seq = list(map(int, input().split()))
D = [0] * n

for i in range(n):
    # 가장 왼쪽에 있는 노드에 저장된 idx 정보 검사
    if q and q[0][1] < i-l+1:
        q.popleft()

    v = seq[i]
    # 가장 오른쪽에 있는 도드에 저장된 val 정보 검사
    while q and q[-1][0] >= v:
        q.pop()
       
    q.append((v,i))
    D[i] = q[0][0]
    
print(*D)