class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.max_length = float('-inf')
        self.max_left = float('-inf')

    def traversal(self, node, length):
        if node.left is None and node.right is None:
            if length > self.max_length:
                self.max_length = length
                self.max_left = node.val

        if node.left:               # 此题一定先找到同一层的最左边的节点，因为是中左右的遍历顺序，同一层的时候一定先从最左边开始遍历
            length += 1             # 所以如果同一层有两个节点，不会进入 length > self.max_length
            self.traversal(node.left, length)
            length -= 1

        if node.right:
            length += 1
            self.traversal(node.right, length)
            length -= 1
        return

    def findBottomLeftValue(self, root: TreeNode) -> float:

        if root is not None:
            self.traversal(root, 0)

        return self.max_left


class Solution2:
    """
    Time O(n)
    层序遍历，每次记录每一层第一个数值，最终就是最后一层最左边节点数值
    """
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = []
        if root is not None:
            queue.append(root)
        else:
            return 0

        left = 0

        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                front = queue.pop(0)
                if i == 0:
                    left = front.val

                if front.left:
                    queue.append(front.left)

                if front.right:
                    queue.append(front.right)

        return left
