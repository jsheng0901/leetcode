class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(inorder, inorder_begin, inorder_end, preorder, preorder_begin, preorder_end):
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
    left_preorder_end = preorder_begin + 1 + delimiter_index - inorder_begin
    # 前序右区间, 左闭右开[rightPreorderBegin, rightPreorderEnd)
    right_preorder_begin = preorder_begin + 1 + (delimiter_index - inorder_begin)
    right_preorder_end = preorder_end

    root_node.left = traversal(inorder, left_inorder_begin, left_inorder_end, preorder, left_preorder_begin,
                               left_preorder_end)
    root_node.right = traversal(inorder, right_inorder_begin, right_inorder_end, preorder, right_preorder_begin,
                                right_preorder_end)

    return root_node


def buildTree(inorder: [int], preorder: [int]) -> TreeNode:
    if len(inorder) == 0 or len(preorder) == 0:
        return None

    return traversal(inorder, 0, len(inorder), preorder, 0, len(preorder))


print(buildTree(inorder=[9, 3, 15, 20, 7], preorder=[9, 15, 7, 20, 3]).val)
