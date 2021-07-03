# Definition for a binary tree node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(root: 'Node') -> int:
    queue = []
    if root is not None:
        queue.append(root)
    depth = 0

    while len(queue) > 0:
        size = len(queue)
        depth += 1
        for i in range(size):
            front_node = queue.pop(0)
            if front_node.children:
                for j in range(len(front_node.children)):
                    if front_node.children[j]:
                        queue.append(front_node.children[j])

    return depth


t1 = Node(val=1)
t2 = Node(val=2)
t3 = Node(val=3)
t4 = Node(val=4)
t1.children = [t2, t3, t4]
print(maxDepth(t1))