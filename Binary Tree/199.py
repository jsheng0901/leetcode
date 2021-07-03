# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: TreeNode) -> [[int]]:
    """
    层序遍历，及一层一层的读取二叉树的数值，从左到右过一遍记录下来
    """
    quene = []
    if root is not None:
        quene.append(root)

    results = []
    while len(quene) > 0:
        size = len(quene)
        # 这里一定要使用固定大小size，不要使用que.size()，因为que.size是不断变化的
        for i in range(size):           # loop每一层的tree node
            front_node = quene.pop(0)
            if i == size - 1:           # 这里判断一下此时的node是不是最右边及每一层最后一个node
                results.append(front_node.val)
            if front_node.left:
                quene.append(front_node.left)
            if front_node.right:
                quene.append(front_node.right)

    return results


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t1.left = t2
t1.right = t3
print(rightSideView(t1))
