#шоста
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
    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = Node(val)
                break
            curr = curr.left
        elif val > curr.val:
            if curr.right is None:
                curr.right = Node(val)
                break
            curr = curr.right
        else:
            break  # вже існує
    return root

def collect_branches(node, result):
    if node is None:
        return
    if node.left and node.right:
        result.append(node.val)
    collect_branches(node.left, result)
    collect_branches(node.right, result)

def main():
    nums = list(map(int, input().split()))
    root = None
    for num in nums:
        if num == 0:
            break
        root = insert(root, num)

    branches = []
    collect_branches(root, branches)
    branches.sort()
    print(*branches)

main()