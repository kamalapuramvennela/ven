class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root or not p or not q:
        return None
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root


bst1 = TreeNode(6)
bst1.left = TreeNode(2)
bst1.right = TreeNode(8)
bst1.left.left = TreeNode(0)
bst1.left.right = TreeNode(4)
bst1.left.right.left = TreeNode(3)
bst1.left.right.right = TreeNode(5)
bst1.right.left = TreeNode(7)
bst1.right.right = TreeNode(9)


node_p1 = bst1.left
node_q1 = bst1.right


result1 = lowest_common_ancestor(bst1, node_p1, node_q1)
if result1:
    print(int(result1.val))
else:
    print("Example 1 - No Common Ancestor found.")


bst2 = TreeNode(6)
bst2.left = TreeNode(2)
bst2.right = TreeNode(8)
bst2.left.left = TreeNode(0)
bst2.left.right = TreeNode(4)
bst2.left.right.left = TreeNode(3)
bst2.left.right.right = TreeNode(5)
bst2.right.left = TreeNode(7)
bst2.right.right = TreeNode(9)


node_p2 = bst2.left
node_q2 = bst2.left.right


result2 = lowest_common_ancestor(bst2, node_p2, node_q2)
if result2:
    print(int(result2.val))
else:
    print("Example 2 - No Common Ancestor found.")


bst3 = TreeNode(2)
bst3.left = TreeNode(1)


node_p3 = bst3
node_q3 = bst3.left


result3 = lowest_common_ancestor(bst3, node_p3, node_q3)
if result3:
    print(int(result3.val))
else:
    print("Example 3 - No Common Ancestor found.")
