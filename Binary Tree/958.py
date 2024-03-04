# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        Time O(n)
        Space O(n)
        层序遍历，记录找到空节点后，是否后面还有节点，如果有说明要么某一层不是完整的节点，要么最后一层不是都在左边。
        注意这里空节点要入列队才能判断。
        """
        queue = [root]
        # 记录是否找到空节点
        null_node_find = False

        while queue:
            node = queue.pop(0)
            # 如果弹出空节点
            if node is None:
                # 标记找到
                null_node_find = True
            else:
                # 如果当前节点不是空节点但是已经找到过空节点说明不符合要求，直接返回false
                if null_node_find:
                    return False
                # 空节点也要入列队
                queue.append(node.left)
                queue.append(node.right)

        return True


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
s = Solution()
print(s.isCompleteTree(node1))
