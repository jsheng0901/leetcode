# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Codec:
    """
    Time O(n)
    Space O(n)
    此题和297基本思路一样，只是这里没有左右子树而是多子树。需要在每个节点后面记录children的size，反序列的时候用来track是否找全所有children
    前序遍历的特点是根节点在开头，然后接着左子树的前序遍历结果，然后接着右子树的前序遍历结果。
    所以我们这里用前序遍历记录所有节点的顺序再转化成string，之后再反序列构建树。这里不需要记录空节点，因为如果children是空则不会进入递归。
    细节见注释
    """

    def _serialize(self, root, sb):
        # 用来处理特殊情况输入是空节点的时候
        if not root:
            return ""

        # 记录当前节点value
        sb.append(str(root.val))
        # 这里要用一个符合记录value和size的区分，不然后续不好拿value和size，因为用index的话很容易拿错value比如 value=11 size=1
        sb.append(",")
        sb.append(str(len(root.children)))
        # 用另一个符合表示当前节点结束了，用于后续split用
        sb.append("#")

        # 遍历children
        for child in root.children:
            self._serialize(child, sb)

        return

    def serialize(self, root: 'Node') -> str:
        sb = []
        self._serialize(root, sb)
        # 返回string
        return "".join(sb)

    def _deserialize(self, nodes):
        if not nodes:
            return None

        node = nodes.pop(0)
        # 当前节点的value和size，这里符合发挥作用
        val, child_size = node.split(',')

        root = Node(int(val))
        child = []
        size = 0
        # 持续记录当前节点的children是否找完全了
        while size < int(child_size):
            tmp = self._deserialize(nodes)
            # 最后一个可能会出现空string，需要判断一下这里
            if tmp:
                child.append(tmp)
                size += 1
        # 赋值
        root.children = child
        # 返回当前节点
        return root

    def deserialize(self, data: str) -> 'Node':
        # 特殊情况输入是空节点，直接返回None
        if len(data) == 0:
            return None
        # split每个节点的记录
        nodes = data.split("#")

        return self._deserialize(nodes)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)
node1.children = [node2, node3, node4, node5]
node3.children = [node6, node7]
node4.children = [node8]
node5.children = [node9, node10]
node7.children = [node11]
node8.children = [node12]
node9.children = [node13]
node11.children = [node14]
codec = Codec()
node1_new = []
print(codec.deserialize(codec.serialize(node1)))
print(codec.deserialize(codec.serialize(node1_new)))
