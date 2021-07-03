class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        层序遍历的模板，只是每次记录每一层的头结点，并且如果不是头结点，就让头结点指向这个节点，然后更新previous node到现在这个节点
        :param root:
        :return:
        """
        queue = []
        if root is not None:
            queue.append(root)

        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                if i == 0:
                    pre = queue.pop(0)
                    node = pre
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