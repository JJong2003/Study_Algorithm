class Node:
    def __init__(self, key):
        self.key = key
        self.left_node = None
        self.right_node = None


class BST:
    def __init__(self, n):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add_recursive(self.root, Node(key))

    def _add_recursive(self, current, node):
        if node.key < current.key:
            if current.left_node is None:
                current.left_node = node
            else:
                self._add_recursive(current.left_node, node)
        else:
            if current.right_node is None:
                current.right_node = node
            else:
                self._add_recursive(current.right_node, node)

    # bottom - up 방식으로
    def solve(self, current):
        if current is None:
            return 0, 1 #노드의 개수, 경우의 수

        left = self.solve(current.left_node)
        right = self.solve(current.right_node)

        cnt_node = 1 + left[0] + right[0]
        cnt_case = self.combination_repetition(left[0]+1, right[0]) * left[1] * right[1]

        return (cnt_node, cnt_case%9999991)

    def countChildren(self, node):
        return (node.left_node is not None)*1 + (node.right_node is not None)*1

    def combination(self, n, r):
        if r < 0 or r > n:
            return 0

        r = min(r, n - r)
        ret = 1
        for i in range(1, r+1):
            ret *= (n - i + 1)
            ret //= i
        return ret

    def combination_repetition(self, n, r):
        return self.combination(n+r-1, r)


tc = int(input())
for _ in range(tc):
    n = int(input())
    bst = BST(n)

    keys = list(map(int, input().split()))
    for key in keys:
        bst.add(key)

    result = bst.solve(bst.root)
    print(result[1])