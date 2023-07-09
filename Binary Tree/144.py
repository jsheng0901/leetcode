# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(tree_node, results):
    if tree_node is None:  # 判读自己现在的node是不是None就可以，及当前node的value会append进result
        return
    results.append(tree_node.val)  # 中间节点
    traversal(tree_node.left, results)  # 左节点
    traversal(tree_node.right, results)  # 右节点


def preorderTraversal(root: TreeNode) -> [int]:
    """
    Time O(n)
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


class Solution:
    """
    二叉树的前序遍历，stack迭代法统一写法
    与上面的区别在于每次处理中间节点的时候用空节点标记一下，当拿到空节点的时候说明是中间节点，此时记录value
    """

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node is not None:
                if node.right:  # 右
                    st.append(node.right)
                if node.left:  # 左
                    st.append(node.left)
                st.append(node)  # 中
                st.append(None)
            else:
                node = st.pop()
                result.append(node.val)
        return result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t1.left = t2
t1.right = t3
print(preorderTraversalStack(t1))
