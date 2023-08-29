from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        # 存储 postorder 中值到索引的映射
        self.value_to_index = {}

    def build(self, preorder, pre_start, pre_end, postorder, post_start, post_end):
        if pre_start > pre_end:
            return None
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        # root 节点对应的值就是前序遍历数组的第一个元素
        root_value = preorder[pre_start]
        # root.left 的值是前序遍历第二个元素
        # 通过前序和后序遍历构造二叉树的关键在于通过左子树的根节点
        # 确定 preorder 和 postorder 中左右子树的元素区间
        left_root_value = preorder[pre_start + 1]
        # left_root_value 在后序遍历数组中的索引
        post_index = self.value_to_index[left_root_value]
        # 左子树的元素个数
        left_size = post_index - post_start + 1

        # 根据左子树的根节点索引和元素个数推导左右子树的索引边界
        # 左子树的前序后续开始结束index
        pre_start_left = pre_start + 1
        pre_end_left = pre_start + left_size
        post_start_left = post_start
        post_start_end = post_index
        # 右子树的前序后续开始结束index
        pre_start_right = pre_start + left_size + 1
        pre_end_right = pre_end
        post_start_right = post_index + 1
        post_end_right = post_end - 1
        # 先构造出当前根节点
        root = TreeNode(root_value)
        # 左右递归构造子树
        root.left = self.build(
            preorder, pre_start_left, pre_end_left, postorder, post_start_left,
            post_start_end
        )

        root.right = self.build(
            preorder, pre_start_right, pre_end_right, postorder, post_start_right,
            post_end_right
        )

        return root

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        通过前序后序遍历结果无法确定唯一的原始二叉树。返回任意一个结果都行。
        1、首先把前序遍历结果的第一个元素或者后序遍历结果的最后一个元素确定为根节点的值。
        2、然后把前序遍历结果的第二个元素作为左子树的根节点的值。
        3、在后序遍历结果中寻找左子树根节点的值，从而确定了左子树的索引边界，进而确定右子树的索引边界，递归构造左右子树即可。
        """
        # 存储 postorder 中值到索引的映射
        for i in range(len(postorder)):
            self.value_to_index[postorder[i]] = i

        return self.build(
            preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1
        )


s = Solution()
print(s.constructFromPrePost(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1]))
