from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.res = 0

    def is_pseudo_palindromic(self, path):
        odd_number = 0

        for i in range(1, len(path)):
            if path[i] % 2 != 0:
                odd_number += 1

                if odd_number > 1:
                    return False

        return odd_number == 1 or odd_number == 0

    def traversal(self, node, path):
        # 遇到空节点
        if node is None:
            return

        # 遇到叶子结点
        if node.left is None and node.right is None:
            # 记录叶子结点频率
            path[node.val] += 1
            # 检查是否是回文
            if self.is_pseudo_palindromic(path):
                # 计数器 +1
                self.res += 1
            # 离开当前叶子节点，回溯
            path[node.val] -= 1
            return

        # 记录当前节点频率
        path[node.val] += 1

        self.traversal(node.left, path)
        self.traversal(node.right, path)

        # 离开当前节点，回溯
        path[node.val] -= 1

        return

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)       since path is constant length no more than 10
        Space O(h)
        前序遍历存储所有节点的值出现的频率，走到叶子节点的时候check是否所有出现的频率只有一个奇数或者没有奇数，如果是则说明是
        pseudo palindromic。同时计数器 +1，如果不是结束此path的search。注意这里因为要一直记录出现的频率，离开此节点的时候要回溯一下，
        因为另一条path不可能包含此节点的值。
        """
        path = [0] * 10
        self.traversal(root, path)

        return self.res


class Solution2:
    def __init__(self):
        self.res = 0

    def traversal(self, node, path):
        if node is None:
            return

        if node.left is None and node.right is None:
            # compute occurrences of each digit
            # in the corresponding register
            # 这里 << 是 left shift，比如节点是3，那就是1的二进制表达式往左边移动3位，这样3这个地方就是二进制表达的1了
            # ^ 代表两个数只有二进制每个位置都是一样的才能是0，不然就是1，也就是同一个节点出现的value只能出现偶数次，奇数次的话对应的
            # 二进制位置就是1，最后再check一遍是不是整个二进制表达式里面最多只有一个1存在，是的话说明符合条件，不是的话跳过此path。
            path = path ^ (1 << node.val)
            # check if at most one digit has an odd frequency
            # 二进制 -1 会把原本的二进制表达式中最后一个1变成0然后1后面的都变成1，& 在二进制里面会对每一位执行同时是1才可以结果是1的逻辑
            # 也就是说原先是1的位置变成了0，后面的所有变成了1，&后原先是1的位置开始因为全都相反了，则都会变成0，此时如果二进制全都是0了
            # 也就是说明当前数字10进制表达是0
            if path & (path - 1) == 0:
                self.res += 1
            return

        path = path ^ (1 << node.val)
        self.traversal(node.left, path)
        self.traversal(node.right, path)

        return

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        思路和第一个一模一样，只是这里用位运算的方式记录每个value出现的频率，同时check是不是最多一个1在出现的频率里面。
        这样check合理的path的时候可以把时间压缩到绝对O(1)，虽然check9位的list理论上也O(1)，但是实际中还是要遍历整个数组，只是数组小。
        当题目需要压缩到O(1)的空间或者只有1-9个数的时候，可以考虑位运算的思路。
        """
        self.traversal(root, 0)

        return self.res


node1 = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(3)
node6 = TreeNode(2)
node6.left = node4
node6.right = node1
node4.left = node5
node4.right = node2
node1.right = node3
s = Solution2()
print(s.pseudoPalindromicPaths(node6))
