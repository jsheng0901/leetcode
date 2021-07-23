# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        中序遍历，同时用x, y来记录需要swap的node，同时用prev指针来双指针同时中序遍历，找到x, y后，直接交换value即可
        无需真正交换指针位置
        """

        def find_two_swapped(root: TreeNode):
            nonlocal x, y, pred
            if root is None:
                return

            find_two_swapped(root.left)
            if pred and root.val < pred.val:
                y = root
                # first swap occurence
                if x is None:
                    x = pred
                    # second swap occurence
                else:
                    return
            pred = root
            find_two_swapped(root.right)

        x = y = pred = None
        find_two_swapped(root)
        x.val, y.val = y.val, x.val

#         def inorder(r: TreeNode) -> List[int]:
#             return inorder(r.left) + [r.val] + inorder(r.right) if r else []

#         def find_two_swapped(nums: List[int]) -> (int, int):
#             n = len(nums)
#             x = y = -1
#             for i in range(n - 1):
#                 if nums[i + 1] < nums[i]:
#                     y = nums[i + 1]
#                     # first swap occurence
#                     if x == -1:
#                         x = nums[i]
#                     # second swap occurence
#                     else:
#                         break
#             return x, y

#         def recover(r: TreeNode, count: int):
#             if r:
#                 if r.val == x or r.val == y:
#                     r.val = y if r.val == x else x
#                     count -= 1
#                     if count == 0:
#                         return
#                 recover(r.left, count)
#                 recover(r.right, count)

#         nums = inorder(root)
#         x, y = find_two_swapped(nums)
#         recover(root, 2)


