import sys
sys.setrecursionlimit(200000)

class Node:
    def init(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def is_balanced(root):
    def check(node):
        if node is None:
            return 0, True
        left_height, left_bal = check(node.left)
        right_height, right_bal = check(node.right)
        height = 1 + max(left_height, right_height)
        balanced = left_bal and right_bal and abs(left_height - right_height) <= 1
        return height, balanced
    _, balanced = check(root)
    return balanced

# Зчитування
nums = list(map(int, input().split()))
root = None
for num in nums:
    if num == 0:
        break
    root = insert(root, num)

# Вивід результату
print("YES" if is_balanced(root) else "NO")