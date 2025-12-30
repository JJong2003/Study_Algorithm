import sys
sys.setrecursionlimit(10**6)

def sol():
    n = int(input())
    preorder = input().split()
    inorder = input().split()
    indexing = {inorder[i]:i for i in range(n)}

    def divide_conquer(p_left, p_right, i_left, i_right):
        if p_left > p_right or i_left > i_right:
            return
        if i_left == i_right:
            print(inorder[i_left], end=' ')
            return

        root = preorder[p_left]
        mid = indexing[root]

        size = mid - i_left

        divide_conquer(p_left + 1, p_left + size, i_left, mid - 1)
        divide_conquer(p_left + size + 1, p_right, mid + 1, i_right)
        print(root, end=' ')

    divide_conquer(0, n-1, 0, n-1)
    print()


if __name__ == '__main__':
    repeat = int(input())
    for _ in range(repeat):
        sol()
