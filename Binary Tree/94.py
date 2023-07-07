# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(tree_node, results):
    if tree_node is None:
        return
    traversal(tree_node.left, results)  # 左节点
    results.append(tree_node.val)  # 中间节点
    traversal(tree_node.right, results)  # 右节点


def inorderTraversal(root: TreeNode) -> [int]:
    """
    二叉树的中序遍历，前序顾名思义就是每个二叉树的中间节点在中间的时候进行读取，顺序为左中右
    """
    results = []
    traversal(root, results)

    return results


def inorderTraversalStack(root: TreeNode) -> [int]:
    """pointer plush stack"""
    stack = []
    curr = root
    result = []

    while len(stack) > 0 or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

    return result


class Solution:
    """
    二叉树的中序遍历，stack迭代法统一写法
    同前序遍历每次处理中间节点的时候用空节点标记一下，当拿到空节点的时候说明是中间节点，此时记录value
    """
    def inorderTraversal(self, root: TreeNode) -> [int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node is not None:
                if node.right:  # 添加右节点（空节点不入栈）
                    st.append(node.right)

                st.append(node)  # 添加中节点
                st.append(None)  # 中节点访问过，但是还没有处理，加入空节点做为标记。

                if node.left:  # 添加左节点（空节点不入栈）
                    st.append(node.left)
            else:  # 只有遇到空节点的时候，才将下一个节点放进结果集
                node = st.pop()  # 重新取出栈中元素
                result.append(node.val)  # 加入到结果集
        return result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t1.left = t2
t1.right = t3
print(inorderTraversalStack(t1))
