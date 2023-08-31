from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node, limit, cur_sum):
        # 走到空节点，直接返回None
        if node is None:
            return None
        # 记录当前root到node总和
        cur_sum += node.val
        # 走到叶子结点，判断是否满足limit需求，满足则返回自己，不满足返回None
        if node.left is None and node.right is None:
            if cur_sum < limit:
                return None
            else:
                return node
        # 左右子树直接赋值
        node.left = self.traversal(node.left, limit, cur_sum)
        node.right = self.traversal(node.right, limit, cur_sum)
        # 赋值后判断此节点是不是唯一一条path并且此path不满足limit需求，如果左右都是None说明此节点也需要删除
        # 如果左右子树有一个满足limit需求，则保留此节点，返回自己。
        if node.left is None and node.right is None:
            return None
        else:
            return node

    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n) recursive stack space
        记录到每一个node时候的current sum，如果到了leaf，则判断是否满足条件，不满足直接返回None，删除节点。满足则返回本身。
        核心是前序遍历逻辑，区别在于，拿到当前节点左右子结果之后，需要判断中间节点逻辑是否需要返回本身或者删除此节点。
        """
        return self.traversal(root, limit, 0)


