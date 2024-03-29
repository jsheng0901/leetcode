from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def connect(self, root: TreeNode) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        层序遍历的模板，只是每次记录每一层的头结点，并且如果不是头结点，就让头结点指向这个节点，然后更新previous node到现在这个节点
        """
        queue = []
        if root is not None:
            queue.append(root)

        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                # 如果是每一层的第一个node，则记录pre指针和cur指针到这个node
                if i == 0:
                    pre = queue.pop(0)
                    node = pre
                # 如果不是第一个node，则开始链接pre指针到当前指针
                else:
                    node = queue.pop(0)
                    pre.next = node
                    pre = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            node.next = None

        return root


class Solution2:
    def traversal(self, node1, node2):
        if node1 is None and node2 is None:
            return

        node1.next = node2

        self.traversal(node1.left, node1.right)
        self.traversal(node2.left, node2.right)
        self.traversal(node1.right, node2.left)

    def connect(self, root: TreeNode) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        前序遍历的写法，思考每一层中间节点需要做什么，需要把当前节点左节点的的左右相连，当前节点的右节点的左右相连，当前节点的左节点右节点相连
        """
        if root is None:
            return root

        self.traversal(root.left, root.right)

        return root


class Solution3:
    def traversal(self, node):
        if node is None:
            return
        # 当前节点左节点链接
        if node.left:
            node.left.next = node.right
        # 当前节点右节点链接
        if node.right:
            # check当前节点是否有next节点
            if node.next:
                node.right.next = node.next.left
            else:
                node.right.next = None

        self.traversal(node.left)
        self.traversal(node.right)

    def connect(self, root: TreeNode) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        前序遍历的另一种写法，每次递归只传入当前节点，
        """
        self.traversal(root)

        return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
s = Solution3()
print(s.connect(root=node1))
