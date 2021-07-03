class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(node, path, result):
    """
    单层递归逻辑
    """
    path.append(str(node.val))
    # 这才到了叶子节点
    if node.left is None and node.right is None:
        # 把所有之前记录的path的节点的value都连接起来
        string_path = "->".join(path)
        result.append(string_path)
        return
    # 回溯要和递归永远在一起，世界上最遥远的距离是你在花括号里，而我在花括号外！用递归的时候一定有回溯
    if node.left:
        traversal(node.left, path, result)
        path.pop()     # 此时回溯到上一个节点，因为当return时说明已经找到叶子节点，我们需要回到这个叶子节点的父节点，及弹出最后一个val

    if node.right:
        traversal(node.right, path, result)
        path.pop()     # 道理同上


def binaryTreePaths(root: TreeNode) -> [str]:
    """
    此题递归和回溯同时用到， 先递归找到同时None的节点时候在回溯
    """
    result = []
    path = []
    if root is None:
        return result

    traversal(root, path, result)

    return result


def binaryTreePathsStack(root: TreeNode) -> [str]:
    """
    stack 方法解题
    """
    stack = []    # 记录节点
    path = []     # 记录节点的path的value
    result = []   # 记录最终结果

    if root is None:
        return result

    stack.append(root)
    path.append(str(root.val))

    while len(stack) > 0:
        top_node = stack.pop()
        string_path = path.pop()   # 一定要在这里pop出来路径，否则回溯的位置不正确，每一次path记录的是一个string “1->2->3",不是单个数字

        if top_node.left is None and top_node.right is None:
            result.append(string_path)

        if top_node.right:
            stack.append(top_node.right)
            path.append(string_path + "->" + str(top_node.right.val))

        if top_node.left:
            stack.append(top_node.left)
            path.append(string_path + "->" + str(top_node.left.val))

    return result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
print(binaryTreePathsStack(t1))
