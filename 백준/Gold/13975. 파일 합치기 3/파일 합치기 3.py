from heapq import heappop, heappush, heapify

def sol(K):
    chters = list(map(int, input().split()))
    heapify(chters)
    tmp = []
    while len(chters) > 1:
        a = heappop(chters)
        b = heappop(chters)
        
        heappush(chters, a + b)
        tmp.append(a+b)
        
    return chters[0] + sum(tmp[:-1])

T = int(input())
for _ in range(T):
    print(sol(int(input())))