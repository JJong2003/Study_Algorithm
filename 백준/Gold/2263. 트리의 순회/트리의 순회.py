import sys
sys.setrecursionlimit(10**6)
    
n = int(input())
in_order = input().split()  # left root right
post_order = input().split()  # left right root
indexing = {in_order[i]: i for i in range(n)}


def preorder(i_left, i_right, p_left, p_right):
    root = post_order[p_right]

    if i_left > i_right or p_left > p_right:
        return

    if i_left == i_right:
        print(in_order[i_left], end=" ")
        return

    mid = indexing[root]
    size = mid - i_left

    print(root, end=" ")
    preorder(i_left, mid - 1, p_left, p_left + size - 1)
    preorder(mid + 1, i_right, p_left + size, p_right - 1)


preorder(0, n - 1, 0, n - 1)