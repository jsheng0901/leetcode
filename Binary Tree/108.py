class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(nums, left, right) -> 'TreeNode':
    """
    构造二叉搜索树，按照中间分开的方式，左边及时左孩子，右边是右孩子
    :param nums:
    :param left:
    :param right:
    :return:
    """
    if left > right:
        return None

    mid = left + ((right - left) // 2)
    root = TreeNode(nums[mid])
    root.left = traversal(nums, left, mid - 1)
    root.right = traversal(nums, mid + 1, right)

    return root


def sortedArrayToBST(nums: [int]) -> TreeNode:
    return traversal(nums, 0, len(nums) - 1)


print(sortedArrayToBST(nums=[-20, -10, -3, -2, 0, 5, 7, 9, 12]).val)
