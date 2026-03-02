from bisect import bisect_left

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

idxs = []
min_var = float('inf')

for i in range(n-2):
    for j in range(i+1, n-1):
        two_sum = liquid[i] + liquid[j]

        idx = bisect_left(liquid, -two_sum, j+1, n-1)

        for k in [idx, idx-1]:
            if j < k < n:
                val = abs(two_sum + liquid[k])
                if val < min_var:
                    min_var = val
                    idxs = [i, j, k]
for i in idxs:
    print(liquid[i], end=' ')