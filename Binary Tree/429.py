class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: Node) -> [[int]]:
    """
    同二叉树的层序loop，只是每一层的个数不一定
    """
    queue = []
    if root is not None:
        queue.append(root)

    results = []
    while len(queue) > 0:
        size = len(queue)
        vector = []
        # 这里一定要使用固定大小size，不要使用que.size()，因为que.size是不断变化的
        for i in range(size):     # loop每一层的tree node
            front_node = queue.pop(0)
            vector.append(front_node.val)
            if front_node.children:
                for j in range(len(front_node.children)):     # 此处要loop过所有的children node并加入到queue里面
                    if front_node.children[j]:
                        queue.append(front_node.children[j])
        results.append(vector)

    return results


t1 = Node(val=1)
t2 = Node(val=2)
t3 = Node(val=3)
t4 = Node(val=4)
t1.children = [t2, t3, t4]
print(levelOrder(t1))