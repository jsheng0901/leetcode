class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getNodeNumber(node):
    if node is None:
        return 0

    left_number = getNodeNumber(node.left)       # 左
    right_number = getNodeNumber(node.right)     # 右
    depth = 1 + left_number + right_number       # 中

    return depth


def countNodes(root: TreeNode) -> int:
    """
    依然是后序遍历，此题同最大深度，每次遍历一颗tree的时候记录左右两边的节点数量再加上中间节点自己
    """
    return getNodeNumber(root)


def countNodesQueue(root: TreeNode):
    """
    层序遍历queue方法
    """
    queue = [root]
    node_number = 0

    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            node_number += 1
            front_node = queue.pop(0)
            if front_node.left:
                queue.append(front_node.left)
            if front_node.right:
                queue.append(front_node.right)

    return node_number


class Solution:
    #     def getNodeNumber(self, node):        # 后序遍历方法
    #         if node is None:
    #             return 0

    #         left = self.getNodeNumber(node.left)
    #         right = self.getNodeNumber(node.right)

    #         number = left + right + 1

    #         return number

    def countNodes(self, root: TreeNode) -> int:
        """
        完全二叉树，利用数学公式计算node 个数，找到full binary tree的时候就直接计算个数
        :param root:
        :return:
        """
        if not root:
            return 0

        left = root.left
        right = root.right
        left_height = 1
        right_height = 1
        while left:
            left = left.left
            left_height += 1
        while right:
            right = right.right
            right_height += 1

        if left_height == right_height:
            return 2 ** left_height - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
print(countNodesQueue(t1))