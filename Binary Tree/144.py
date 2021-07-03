# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(tree_node, results):
    if tree_node is None:                   # 判读自己现在的node是不是None就可以，及当前node的value会append进result
        return
    results.append(tree_node.val)           # 中间节点
    traversal(tree_node.left, results)      # 左节点
    traversal(tree_node.right, results)     # 右节点


def preorderTraversal(root: TreeNode) -> [int]:
    """
    二叉树的前序遍历，前序顾名思义就是每个二叉树的中间节点在最开始的时候进行读取，顺序为中左右
    """
    results = []
    traversal(root, results)

    return results


def preorderTraversalStack(root: TreeNode) -> [int]:
    """
    二叉树的前序遍历，stack 迭代法
    """
    stack = []
    results = []

    cur = root
    stack.append(cur)

    while len(stack) > 0:
        node = stack.pop()
        results.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return results


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t1.left = t2
t1.right = t3
print(preorderTraversalStack(t1))
