# Definition for a binary tree node.
from typing import List


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


class Solution:
    """
    二叉树的后序遍历，stack迭代法统一写法
    同前序遍历每次处理中间节点的时候用空节点标记一下，当拿到空节点的时候说明是中间节点，此时记录value
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node is not None:
                st.append(node)  # 中
                st.append(None)

                if node.right:  # 右
                    st.append(node.right)
                if node.left:  # 左
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result


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
