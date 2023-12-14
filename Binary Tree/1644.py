from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        # 全局变量记录是否找到两个节点
        self.p_flag = False
        self.q_flag = False

    def traversal(self, node, p, q):
        # 走到底，返回 None
        if node is None:
            return node

        # 后续遍历先拿返回值
        left = self.traversal(node.left, p, q)
        right = self.traversal(node.right, p, q)

        # 如果当前节点是p，则直接返回，并标记上
        if node == p:
            self.p_flag = True
            return node
        # 如果当前节点是q，则直接返回，并标记上
        if node == q:
            self.q_flag = True
            return node
        # 如果当前节点不是p q，但是子节点都存在，说明当前节点是父节点，返回当前节点
        if left is not None and right is not None:
            return node
        # 如果当前节点不是p q，但是子节点某一个存在，返回存在节点
        elif left is None and right is not None:
            return right
        # 同上
        elif right is None and left is not None:
            return left
        # 当前节点和子节点都不是我要找的节点，返回None
        else:
            return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        """
        Time O(n)
        Space O(n)
        同理236，区别在于当我们遇到p q节点得到时候我们不能停止遍历直接返回节点，因为可能节点下面没有我们要找的另一个节点。
        因为此题目并不保证需要遍历搜索的节点一定在树里面。所以此时应该把前序遍历处理中间节点的位置逻辑移动到后序遍历即可，因为这样我们就会遍历
        完整个树再判断。之后就是一模一样的判断逻辑，先判断当前节点是不是我们要找的，如果是直接返回，这里用一个全局变量标记记录一下我们找到的
        节点，为后续判断是否都找到用。详细见注释
        """
        res = self.traversal(root, p, q)
        # 判断一下是否两个都找到了，如果是说明都存在树里面，返回结果
        if self.p_flag and self.q_flag:
            return res
        # 如果有一个没找到，说明有一个不存在树里面，返回None
        else:
            return None


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t1.left = t3
t4 = TreeNode(4)
s = Solution()
print(s.lowestCommonAncestor(t1, t2, t4))
