from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build(self, nums, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])
        node.left = self.build(nums, left, mid - 1)
        node.right = self.build(nums, mid + 1, right)

        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        构造二叉搜索树，按照中间分开的方式，左边及时左孩子，右边是右孩子
        """
        return self.build(nums, 0, len(nums) - 1)


s = Solution()
print(s.sortedArrayToBST(nums=[-20, -10, -3, -2, 0, 5, 7, 9, 12]).val)
