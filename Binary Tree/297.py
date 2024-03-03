class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """
    Time O(n)
    Space O(n)
    前序遍历的特点是根节点在开头，然后接着左子树的前序遍历结果，然后接着右子树的前序遍历结果。
    所以我们这里用前序遍历记录所有节点的顺序再转化成string，之后再反序列构建树。这里要记录空节点才能确定一棵树，
    如果没有空节点则无法确定树的结构。每个节点之间用逗号隔开方便后面遍历节点。
    """
    def __init__(self):
        self.SEP = ','
        self.NULL = '#'

    # 将二叉树序列化为字符串
    def serialize(self, root: TreeNode) -> str:
        # 记录前序遍历的结果
        sb = []
        self._serialize(root, sb)
        return ''.join(sb)

    # 将二叉树存入列表
    def _serialize(self, root, sb):
        # 空节点，记录特殊字符
        if not root:
            sb.append(self.NULL)
            sb.append(self.SEP)
            return

        # 前序遍历位置
        sb.append(str(root.val))
        sb.append(self.SEP)

        self._serialize(root.left, sb)
        self._serialize(root.right, sb)

    # 将字符串反序列化为二叉树结构
    def deserialize(self, data: str) -> TreeNode:
        # 将字符串转化成列表
        nodes = data.split(self.SEP)
        return self._deserialize(nodes)

    # 通过 nodes 列表构造二叉树
    def _deserialize(self, nodes):
        if not nodes:
            return None

        # 前序遍历位置
        # 这里最大的区别是第一个元素一定是当前节点的值，前序遍历的特点
        val = nodes.pop(0)
        if val == self.NULL:
            return None
        root = TreeNode(int(val))

        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)

        return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
c = Codec()
print(c.deserialize(c.serialize(node1)))
