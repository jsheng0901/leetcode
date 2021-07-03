# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(tree_node, results):
    if tree_node is None:
        return
    traversal(tree_node.left, results)      # 左节点
    traversal(tree_node.right, results)     # 右节点
    results.append(tree_node.val)           # 中间节点


def postorderTraversal(root: TreeNode) -> [int]:
    """
    二叉树的后序遍历，前序顾名思义就是每个二叉树的中间节点在最后的时候进行读取，顺序为左右中
    """
    results = []
    traversal(root, results)

    return results


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t4 = TreeNode(val=4)
t5 = TreeNode(val=5)
t6 = TreeNode(val=6)
t7 = TreeNode(val=7)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
print(postorderTraversal(t1))
