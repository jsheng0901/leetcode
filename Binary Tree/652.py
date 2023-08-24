from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []
        self.record = {}

    def traversal(self, node):
        if node is None:
            return "#"

        left_subtree = self.traversal(node.left)
        right_subtree = self.traversal(node.right)
        # 存储左右子树加自己的序列化结构，用string，中间用分隔符号，不然会出现22 == 2,2其实是两中结构
        subtree = left_subtree + ',' + right_subtree + ',' + str(node.val)
        # 拿到出现频率，出现一次记录一次就好，不需要重复记录，所有只判断freq是不是1
        freq = self.record.get(subtree, 0)
        if freq == 1:
            self.result.append(node)

        self.record[subtree] = freq + 1

        return subtree

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Time O(n^2) 遍历每个节点，每个节点需要粗略遍历所有子节点记录下来
        Space O(n) 额外的存储子树空间
        后续遍历，每次在中间节点判断左右子树加自己是不是出现过，用全局dictionary来存储出现的子树结构，
        这里存储方式用string，来判断是否有相同的子树结构
        """
        self.traversal(root)

        return self.result


node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(1)
node1.left = node2
node1.right = node3

s = Solution()
print(s.findDuplicateSubtrees(root=node1))

