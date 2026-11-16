n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
left, right = 0, 10**10
K = 0
while left+1 < right:
    mid = (left+right)//2

    # 결정 함수
    cnt = 0
    for a in arr:
        cnt += a//mid
    
    # 이분
    if cnt >= m:
        left = mid
        K = max(K, mid)
    else:
        right = mid

print(K)