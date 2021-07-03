# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root: TreeNode) -> [[int]]:
    """
    层序遍历，及一层一层的读取二叉树的数值，从左到右过一遍记录下来
    """
    quene = []
    if root is not None:
        quene.append(root)

    results = []
    while len(quene) > 0:
        size = len(quene)
        vector = []
        for i in range(size):
            front_node = quene.pop(0)
            vector.append(front_node.val)
            if front_node.left:
                quene.append(front_node.left)
            if front_node.right:
                quene.append(front_node.right)

        results.append(vector)

    return results[::-1]          # 同从上至下的层次循环，最后reverse一下即可


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t1.left = t2
t1.right = t3
print(levelOrderBottom(t1))
