import heapq

def solution(n, works):
    h = []
    # O(n lg n)
    for w in works:
        heapq.heappush(h, -w)
    
    # O(n lg n)
    for i in range(n):
        w = -heapq.heappop(h)
        w = max(0, w-1)
        heapq.heappush(h, -w)
    
    ans = 0
    for i in range(len(works)):
        ans += h[i]**2
    print(h)
    return ans