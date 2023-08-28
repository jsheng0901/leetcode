from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def traversal(self, inorder, inorder_begin, inorder_end, preorder, preorder_begin, preorder_end):
        if preorder_begin == preorder_end:
            return None

        root_value = preorder[preorder_begin]
        root_node = TreeNode(root_value)

        if preorder_end - preorder_begin == 1:
            return root_node

        delimiter_index = inorder.index(root_value)
        # 切割中序数组
        # 左闭右开区间：左闭右开[leftInorderBegin, leftInorderEnd)
        left_inorder_begin = inorder_begin
        left_inorder_end = delimiter_index

        # [delimiterIndex + 1, end) 左闭右开[rightInorderBegin, rightInorderEnd)
        right_inorder_begin = delimiter_index + 1
        right_inorder_end = inorder_end

        # 切割前序数组
        # 前序左区间，左闭右开[leftPreorderBegin, leftPreorderEnd)
        left_preorder_begin = preorder_begin + 1
        left_preorder_end = preorder_begin + 1 + (delimiter_index - inorder_begin)
        # 前序右区间, 左闭右开[rightPreorderBegin, rightPreorderEnd)
        right_preorder_begin = preorder_begin + 1 + (delimiter_index - inorder_begin)
        right_preorder_end = preorder_end

        root_node.left = self.traversal(inorder, left_inorder_begin, left_inorder_end, preorder, left_preorder_begin,
                                        left_preorder_end)
        root_node.right = self.traversal(inorder, right_inorder_begin, right_inorder_end, preorder,
                                         right_preorder_begin,
                                         right_preorder_end)

        return root_node

    def buildTree(self, inorder: [int], preorder: [int]) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        前序遍历第一个位置就是root节点，找到节点后，中序遍历找到节点的index，此时中序index左右两边就是左右子树的node，再通过左右子树的
        长度，找到前序数组的相对应的分割点。然后递归返回左右子树赋值。
        """
        if len(inorder) == 0 or len(preorder) == 0:
            return None

        return self.traversal(inorder, 0, len(inorder), preorder, 0, len(preorder))


class Solution2:
    def build(self, preorder, inorder):
        # 第一步: 特殊情况讨论: 树为空. 或者说是递归终止条件.
        if len(preorder) == 0:
            return None

        # 第二步: 前序遍历的第一个就是当前的中间节点.
        value = preorder[0]
        node = TreeNode(value)

        # 第三步: 找切割点.
        index = inorder.index(value)

        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        left_inorder = inorder[:index]
        right_inorder = inorder[index + 1:]

        # 第五步: 切割preorder数组. 得到preorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟前序数组大小是相同的.
        left_preorder = preorder[1:len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]

        # 第六步: 递归,赋值
        node.left = self.build(left_preorder, left_inorder)
        node.right = self.build(right_preorder, right_inorder)

        # 第七步: 返回当前中间节点
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        另一种写法，不通过传输分裂点，直接切割后递归参数传输切割后的数组，找index的时候可以优化一下，不需要loop全数组，可以直接用一个
        hash map记录value和index的关系，找index可以缩短时间到O(1)。但这样每次递归传入的参数必须是切割index而不是切割过的数组。
        """
        return self.build(preorder, inorder)


s = Solution2()
print(s.buildTree(inorder=[9, 3, 15, 20, 7], preorder=[9, 15, 7, 20, 3]).val)
