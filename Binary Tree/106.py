from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        构造树一般采用的是前序遍历，因为先构造中间节点，然后递归构造左子树和右子树。
        """
        if len(postorder) == 0:
            return None

        root_value = postorder[-1]
        root_node = TreeNode(root_value)

        if len(postorder) == 1:
            return root_node

        delimiter_index = inorder.index(root_value)
        # 切割中序数组
        # 左闭右开区间：[0, delimiterIndex)
        left_inorder = inorder[0: 0 + delimiter_index]
        # [delimiterIndex + 1, end)
        right_inorder = inorder[0 + delimiter_index + 1:]

        # postorder
        # 舍弃末尾元素
        postorder.pop()

        # 切割后序数组
        # 依然左闭右开，注意这里使用了左中序数组大小作为切割点
        # [0, leftInorder.size)
        left_postorder = postorder[0:0 + len(left_inorder)]
        # [leftInorder.size(), end)
        right_postorder = postorder[0 + len(left_inorder):]

        root_node.left = self.traversal(left_inorder, left_postorder)
        root_node.right = self.traversal(right_inorder, right_postorder)

        return root_node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        后序遍历最后一个位置就是root节点，找到节点后，中序遍历找到节点的index，此时中序index左右两边就是左右子树的node，再通过左右子树的
        长度，找到后序数组的相对应的分割点。然后递归返回左右子树赋值。同105，只是后序拿中间节点的位置不一样。
        """
        if len(inorder) == 0 or len(postorder) == 0:
            return None

        return self.traversal(inorder, postorder)


s = Solution()
print(s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]).val)
