def _find(literal, value):
    for i in range(len(literal)):
        if literal[i] == value:
            return i
    return 101

n, k = map(int, input().split())
jobs = list(map(int, input().split()))

taps = [-1] * n

ans = 0
for i in range(k):
    job = jobs[i]
    if job in taps:
        continue
    
    for j in range(n):
        if taps[j] == -1:
            taps[j] = job
            break
    else:
        cnts = [0] * (n+1) # 멀티탭 꽂혀 있는 작업에 대해서 뒤에 또 작업이 있는지 확인 있다면 어마나 멀리 있는지?
        
        for j in range(n):
            tap = taps[j]
            idx = _find(jobs[i:], tap)
            cnts[j] = idx
                    
        exchange_idx = _find(cnts, max(cnts[:-1]))
        taps[exchange_idx] = job
        ans += 1
print(ans)
        