class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(inorder, postorder):
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

    root_node.left = traversal(left_inorder, left_postorder)
    root_node.right = traversal(right_inorder, right_postorder)

    return root_node


def buildTree(inorder: [int], postorder: [int]) -> TreeNode:
    if len(inorder) == 0 or len(postorder) == 0:
        return None

    return traversal(inorder, postorder)


print(buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]).val)
