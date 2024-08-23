# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def __init__(self):
        self.res = 0

    def traversal(self, node):
        # 如果节点不存在，直接返回0，加这个会更快点，因为test case里面有空节点存在的情况
        if node is None:
            return 0

        top_1_distance, top_2_distance = 0, 0
        # 遍历邻居节点
        for child in node.children:
            # 当前节点拿到的子节点返回值
            distance = self.traversal(child) + 1

            # 后续遍历位置，用两个指针来接住最长的两个距离
            # 如果大于最长的距离，则更新两个距离
            if distance > top_1_distance:
                # 注意这里一定要先更新第二个距离，再更新第一个，否则顺序颠倒的话第二个距离会等于第一个距离
                top_2_distance = top_1_distance
                top_1_distance = distance
                # 或者采用这种swap的形式写，同一行更新
                # top_1_distance, top_2_distance = distance, top_1_distance
            # 如果大于第二个，则只更新第二个距离
            elif distance > top_2_distance:
                top_2_distance = distance

        # 更新直径
        self.res = max(self.res, top_1_distance + top_2_distance)

        # 返回最长的距离
        return top_1_distance

    def diameter(self, root: 'Node') -> int:
        """
        Time O(n)
        Space O(n)
        此题的思路和1245一模一样，只是这里是树，1245是图，同时是543的进阶版本，我们需要的就是每次返回的时候拿到最长的两个值。
        """

        self.traversal(root)

        return self.res


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node1.children = [node3, node2, node4]
node3.children = [node5, node6]
s = Solution()
print(s.diameter(node1))
