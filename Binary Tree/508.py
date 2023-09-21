from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.freq = defaultdict(int)

    def traversal(self, node):
        if node is None:
            return 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 统计子树和，后序遍历位置
        subtree_sum = left + right + node.val
        self.freq[subtree_sum] += 1

        return subtree_sum

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        后续遍历，每次记录子树的总和，并且记录出现频率。最终loop一遍频率字典，找到出现频率最多的子树和。
        """
        self.traversal(root)

        result = []
        max_value = max(self.freq.values())
        for k, v in self.freq.items():
            if v == max_value:
                result.append(k)

        return result


node1 = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(-2)
node1.left = node2
node1.right = node3
s = Solution()
print(s.findFrequentTreeSum(node1))
