import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST():
    def __init__(self, root):
        self.root = root;

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while current:
            val = current.value
            if val < value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    break
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    break
        return

    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        sys.stdout.write(str(node.value)+'\n')


preorder = []
while 1:
    try:
        k = int(input())
        preorder.append(k)
    except:
        break

root = Node(preorder[0])
bst = BST(root)

for i in range(1, len(preorder)):
    bst.insert(preorder[i])

bst.postorder(root)
sys.stdout.flush()