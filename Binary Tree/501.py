from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def traversal(self, root, freq):
        """
        中序遍历并记录所有数值出现的频率
        """
        if root is None:
            return
        self.traversal(root.left, freq)
        if root.val in freq:        # 将二叉搜索树转换为dictionary存储频率
            freq[root.val] += 1
        else:
            freq[root.val] = 0
        self.traversal(root.right, freq)

    def findMode(self, root: TreeNode) -> [int]:
        """
        Time O(n)
        Space O(n)
        中序遍历，BTS一般饿哦们都采用中序遍历，因为中序遍历出来的结果刚好是从小到大的有序list，此处是dictionary记录频率
        """
        freq = {}
        self.traversal(root, freq)

        # 计算词典中最大的value

        # max_value = max(dict.values())
        # for k, v in dict.items():
        #     if v == max_value:
        #         results.append(k)

        results = max(freq, key=freq.get)

        return results


class Solution2:
    def __init__(self):
        self.result = []
        self.pre = None
        self.count = 1
        self.max_value = 1

    def traversal(self, root):
        if root is None:
            return

        self.traversal(root.left)    # 左
        if self.pre is None:
            self.count = 1
        elif self.pre.val == root.val:
            self.count += 1
        else:
            self.count = 1
        # 记录前一个node
        self.pre = root

        if self.count == self.max_value:    # 如果和最大值相同，放进result中
            self.result.append(root.val)

        if self.count > self.max_value:     # 如果计数大于最大值频率
            self.max_value = self.count     # 更新最大频率
            self.result = []                # 很关键的一步，不要忘记清空result，之前result里的元素都失效了
            self.result.append(root.val)

        self.traversal(root.right)   # 右

    def findMode(self, root: TreeNode) -> List[any]:
        """
        Time O(n)
        Space O(1)
        此方法可以节约空间，不需要额外记录频率，也不需要额外loop一遍dict，记录previous node和current node然后比较频率并更新result
        """

        self.traversal(root)

        return self.result


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(2)
t1.right = t2
t2.left = t3
s = Solution1()
print(s.findMode(t1))
