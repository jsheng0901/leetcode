class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TODO: results will be modified by path when path pop out
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def traversal(self, node, count):
        """
        后序遍历，count是用来判断当前node是否满足总和，用减法来判断，记录所有路径，则不需要返回数值在递归过程中
        """
        if node.left is None and node.right is None and count == 0:
            self.result.append(self.path)
            return
        if node.left is None and node.right is None:
            return

        if node.left:
            self.path.append(node.left.val)  # 递归
            count -= node.left.val  # 此处体现回溯的逻辑，减去后不满足这要加回来，等于回到上一个node
            self.traversal(node.left, count)
            count += node.left.val
            self.path.pop()

        if node.right:
            self.path.append(node.right.val)
            count -= node.right.val  # 此处体现回溯的逻辑，减去后不满足这要加回来，等于回到上一个node
            self.traversal(node.right, count)
            count += node.right.val
            self.path.pop()

        return

    def pathSum(self, root: TreeNode, targetSum: int) -> [[int]]:

        if root is None:
            return self.result

        self.path.append(root.val)
        self.traversal(root, targetSum - root.val)

        return self.result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
solution = Solution()
print(solution.pathSum(t1, 5))
