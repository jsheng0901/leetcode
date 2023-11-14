# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution1:

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Time O(p_parent + q_parent)
        Space O(n)
        loop p parent first, and add it to set, then loop q parent, if meet in set then return
        """
        p_set = set()
        while p:
            p_set.add(p)
            p = p.parent

        while q:
            if q in p_set:
                return q
            q = q.parent

        return None


class Solution2:
    def __init__(self):
        self.lca = None

    def preorder(self, root, node, target):
        if node is None:
            return

        if node.val == target:
            self.lca = root
            return
        self.preorder(root, node.left, target)
        self.preorder(root, node.right, target)

        return

    def postorder(self, p, q, p_path, q_path):
        # 记录走过的节点进set，这里要check节点是否存在先，不然同时同步两个子节点一起走，可能有一个已经走完到root了，root没有parent节点
        if p:
            p_path.add(p.val)
        if q:
            q_path.add(q.val)
        # 如果当前p在q的路径上出现过，说明遇到LCA了，全局变量记录LCA
        if p and p.val in q_path:
            self.lca = p
            return
        # 同理
        elif q and q.val in p_path:
            self.lca = q
            return
        # 更新下一个递归节点父节点，判断一下是否已经走完了
        p_parent = p.parent if p else None
        q_parent = q.parent if q else None
        # 向上父节点递归
        self.postorder(p_parent, q_parent, p_path, q_path)

        return

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Time O(max(p_parent, q_parent))
        Space O(n)
        两种写法，一种直接用同时两个子节点后续遍历所有parent，记录每一个子节点走过的path进set，如果有存在的说明有交集则刚好是LCA。
        另一种是把LCA分成两种情况，一种是子节点在相互的path到leaf的路上，一直是子节点没有相交的path只有公用的父节点，此时对于有公共的path
        情况，可以前序遍历找到LCA，没有公共path的情况同第一种写法后续遍历找公共父节点。同时遍历p，q节点更快，虽然理论上都是O(n)。
        """
        # 此写法是当子节点在相互的path上
        # self.preorder(p, p, q.val)
        #
        # if self.lca is None:
        #     self.preorder(q, q, p.val)
        #     if self.lca is None:
        #         self.postorder(p, q, set(), set())
        #         return self.lca
        #     else:
        #         return self.lca
        # else:
        #     return self.lca
        self.postorder(p, q, set(), set())
        return self.lca


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node3.left = node5
node3.right = node1
node5.parent = node3
node1.parent = node3
node5.left = node6
node5.right = node2
node6.parent = node5
node2.parent = node5
node2.left = node7
node2.right = node4
node7.parent = node2
node4.parent = node2
node1.left = node0
node1.right = node8
node0.parent = node1
node8.parent = node1
s = Solution2()
print(s.lowestCommonAncestor(node5, node1).val)


