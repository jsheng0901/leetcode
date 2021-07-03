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
    results.append(tree_node.val)           # 中间节点
    traversal(tree_node.right, results)     # 右节点


def inorderTraversal(root: TreeNode) -> [int]:
    """
    二叉树的中序遍历，前序顾名思义就是每个二叉树的中间节点在中间的时候进行读取，顺序为左中右
    """
    results = []
    traversal(root, results)

    return results


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t1.left = t2
t1.right = t3
print(inorderTraversal(t1))
