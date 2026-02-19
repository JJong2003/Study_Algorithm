N = int(input())
nodes = list(map(int, input().split()))
sum_nodes = sum(nodes)
S = lambda n, d: n * (n - 1) * d // 2


def get_differ(d):
    ret = 0
    for i in range(d, N * d, d):
        ret += abs(nodes[i // d] - i)
    return ret


low, high = 0, 2 << 63
ans = float('inf')
while low + 2 < high:
    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    a = get_differ(mid1)
    b = get_differ(mid2)
    if a > b:
        low = mid1
    else:
        high = mid2
print(min(a, b))