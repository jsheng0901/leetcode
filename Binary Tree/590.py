# Definition for a binary tree node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def traversal(tree_node, results):
    if tree_node is None:                   # 判读自己现在的node是不是None就可以，及当前node的value会append进result
        return

    if tree_node.children:
        for i in range(len(tree_node.children)):
            traversal(tree_node.children[i], results)      # children节点
    results.append(tree_node.val)  # 中间节点


def postorderTraversal(root: Node) -> [int]:
    """
    二叉树的后序遍历应用，此处没有左右，及从右到左遍历children
    """
    results = []
    traversal(root, results)

    return results


t1 = Node(val=1)
t2 = Node(val=2)
t3 = Node(val=3)
t4 = Node(val=4)
t1.children = [t2, t3, t4]
print(postorderTraversal(t1))
