from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.leaf = []

    def traversal(self, node):
        # 空节点返回 None
        if node is None:
            return None
        # 遇到叶子节点，记录结果，返回 None用于删除叶子结点赋值，前序遍历位置
        if node.left is None and node.right is None:
            self.leaf.append(node.val)
            return None
        # 拿到左右节点的返回结果
        left = self.traversal(node.left)
        right = self.traversal(node.right)
        # 左节点为空则说明左边是叶子结点，赋值删除节点，后续遍历位置
        if left is None:
            node.left = None
        # 右节点同理
        if right is None:
            node.right = None
        # 如果当前节点不是叶子结点，返回原本节点
        return node

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time O(n * (n-leaf1) * (n-leaf2) * ...)
        Space O(n)
        每次遍历后续遍历一次树，找到当前的所有leaves加入list然后赋值删除当前所有leaves，之后继续遍历新的树。直到根节点删除完。
        此方法可以过所有test，可能是因为test case的树并不深。但是其实很多重复操作，并不需要重复遍历叶子结点上面的节点。
        """
        res = []
        # 直到根节点没有删除，继续遍历新的树
        while root:
            self.leaf = []
            root = self.traversal(root)
            res.append(self.leaf)

        return res


class Solution2:
    def __init__(self):
        self.leaf = defaultdict(list)

    def traversal(self, node):
        if node is None:
            return 0

        # 拿到左右子树的高度
        left = self.traversal(node.left)
        right = self.traversal(node.right)
        # 当前节点最大高度
        depth = max(left, right) + 1
        # 记录高度和当前节点值，后续遍历位置
        self.leaf[depth - 1].append(node.val)
        # 返回当前高度
        return depth

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time O(n)
        Space O(n)
        其实此题并不需要真正删除节点，本质上是记录每个节点到最底部的高度，同一高度的节点我们记录到同一个数组内。
        所以我们需要做的是找到每个节点的高度然后用dictionary记录下来，key是高度，value是对应的节点数组。
        最后遍历一次dictionary，insert方式记录进最终结果list。
        """
        res = []
        # 遍历并且记录高度和value关系
        self.traversal(root)
        # 转换dictionary为数组
        for k, v in self.leaf.items():
            res.insert(k, v)

        return res


class Solution3:
    def __init__(self):
        self.leaf = []

    def traversal(self, node):
        if node is None:
            return 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)
        depth = max(left, right) + 1
        # 区别方法2在这里，如果是新的index，则说明是新的高度的第一个元素，insert新的子list
        if len(self.leaf) == depth - 1:
            self.leaf.insert((depth - 1), [node.val])
        # 如果不是，说明之前存在，直接拿出来子数组加进去当前value
        else:
            self.leaf[depth - 1].append(node.val)
        return depth

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time O(n)
        Space O(n)
        同方法2逻辑，只是不需要再次遍历字典，直接在找到高度和value关系的时候存储进最终数组。
        但虽然此方法只需要一次遍历，其实leetcode上面测试更慢，应该是因为测试数据的树并不深，所以方法2多遍历一次字典并不慢，
        然而因为insert在Python里面是O(n)的操作，所以此方法其实更慢。
        """
        self.traversal(root)

        return self.leaf


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
s = Solution3()
print(s.findLeaves(node1))
