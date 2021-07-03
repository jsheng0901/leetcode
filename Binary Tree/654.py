class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums: [int]) -> TreeNode:
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        node = TreeNode(nums[0])
        return node

    # 找到数组中最大的值和对应的下表
    max_value = 0
    max_value_index = 0
    for i in range(len(nums)):
        if nums[i] > max_value:
            max_value = nums[i]
            max_value_index = i

    node = TreeNode(max_value)

    # 最大值所在的下表左区间 构造左子树
    new_nums = nums[:max_value_index]
    node.left = constructMaximumBinaryTree(new_nums)

    # 最大值所在的下表右区间 构造右子树
    new_nums = nums[max_value_index + 1:]
    node.right = constructMaximumBinaryTree(new_nums)

    return node


