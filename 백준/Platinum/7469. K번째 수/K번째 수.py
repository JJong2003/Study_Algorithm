import bisect, sys
input = sys.stdin.readline

def merge(arr):
    if len(arr) < 2: return arr

    mid = len(arr) // 2
    lo_arr = merge(arr[:mid])
    hi_arr = merge(arr[mid:])
    merged_arr = []

    l, h = 0, 0
    while l < len(lo_arr) and h < len(hi_arr):
        if lo_arr[l] < hi_arr[h]:
            merged_arr.append(lo_arr[l])
            l += 1
        else:
            merged_arr.append(hi_arr[h])
            h += 1
    merged_arr += lo_arr[l:]
    merged_arr += hi_arr[h:]
    return merged_arr

def init_tree(start, end, idx=1):
    if start == end:
        tree[idx] = [arr[start]]
        return tree[idx]
    mid = (start + end) // 2
    non_sorted = init_tree(start, mid, idx * 2) + init_tree(mid + 1, end, idx * 2 + 1)
    tree[idx] = merge(non_sorted)

    return tree[idx]

def count_less_or_equal(start, end, left, right, value, idx=1):
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return bisect.bisect_right(tree[idx], value)

    mid = (start+end)//2
    return (count_less_or_equal(start, mid, left, right, value, idx*2) + count_less_or_equal(mid+1, end, left, right, value, idx*2+1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = [[] for _ in range(n * 4)]
    init_tree(0, n - 1)

    for _ in range(m):
        left, right, k = map(int, input().split())
        answer = None
        lo, hi = -(10**9+1), 10**9+1
        while lo<hi-1:
            mid = (lo+hi)//2
            cnt = count_less_or_equal(0, n - 1, left - 1, right - 1, mid)
            if cnt >= k:
                answer = mid
                hi = mid
            else:
                lo = mid
        print(answer)