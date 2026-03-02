from collections import deque

n, l = map(int, input().split())
A = list(map(int, input().split()))

dq = deque() # val, index
ans = []

for i in range(n):
    a = A[i]

    # 값이 a 보다 크다면 모두 제거
    while dq and dq[-1][0] > a:
        dq.pop()

    # 값이 범위 l 바깥이면 제거
    while dq and dq[0][1] < i-l+1:
        dq.popleft()

    dq.append((a, i))
    ans.append(dq[0][0])
    
print(*ans)