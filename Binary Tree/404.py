from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def getSum(self, node):
        if node is None:
            return 0

        left_value = self.getSum(node.left)
        right_value = self.getSum(node.right)

        mid_value = 0
        # 找到node的left节点是左叶子
        if node.left is not None and node.left.left is None and node.left.right is None:
            mid_value = node.left.val

        return left_value + right_value + mid_value

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        后序遍历， 每次判断当前node的left有没有，并且node left的children是否存在，来确定左叶子，同时处理左叶子和，并返回。
        """

        return self.getSum(root)


class Solution2:
    def sumOfLeftLeavesStack(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        后序遍历stack写法，每次判断当前node的left有没有，并且node left的children是否存在，来确定左叶子
        """
        if root is None:
            return 0

        stack = [root]
        result = 0

        while len(stack) > 0:
            top_node = stack.pop()
            if top_node.left is not None and top_node.left.left is None and top_node.left.right is None:
                result += top_node.left.val

            if top_node.right:
                stack.append(top_node.right)

            if top_node.left:
                stack.append(top_node.left)

        return result


class Solution3:
    def __init__(self):
        self.result = 0

    def getLeftSum(self, node, direction):
        if direction == 'left' and node.left is None and node.right is None:
            self.result += node.val
            return

        if node.left:
            self.getLeftSum(node.left, 'left')
        if node.right:
            self.getLeftSum(node.right, 'right')

        return

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        前序遍历写法，遇到符合情况的节点，则加入全局变量记录进result。
        """
        if root:
            self.getLeftSum(root, 'root')

        return self.result


class Solution4:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        层序遍历的方法，遇到属性是左，并且没有子节点的节点，加入进最终结果。
        """

        queue = [(root, 'root')]
        result = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node, direction = queue.pop(0)
                if direction == 'left' and node.left is None and node.right is None:
                    result += node.val
                if node.left:
                    queue.append((node.left, 'left'))
                if node.right:
                    queue.append((node.right, 'right'))

        return result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
s = Solution4()
print(s.sumOfLeftLeaves(t1))
