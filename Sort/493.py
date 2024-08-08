from typing import List


class Solution1:
    def __init__(self):
        self.pairs = 0

    def count(self, left, right):
        # 计算所有符合条件的pairs，遍历所有组合
        for i in left:
            for j in right:
                if i > 2 * j:
                    self.pairs += 1

        return

    def merge_sort(self, nums):
        if len(nums) < 2:
            return
        # 找中间节点
        middle = len(nums) // 2
        # 左右递归
        left = nums[: middle]
        right = nums[middle:]
        self.merge_sort(left)
        self.merge_sort(right)
        # 计算当前左右数组
        self.count(left, right)

        return

    def reversePairs(self, nums: List[int]) -> int:
        """
        Time O(n^2)
        Space O(n)
        利用归并排序的思路，进行分治计算，每一次对比左右数组的时候需要遍历每个元素，所以其实还是O(n^2)的操作。并没有利用到排序完后的优势。
        明显TLE。
        """
        self.merge_sort(nums)

        return self.pairs


class Solution2:
    def __init__(self):
        self.pairs = 0

    def merge_count(self, left, right):
        # 计算有多少个合理的pairs
        p1 = 0
        p2 = 0
        while p1 < len(left) and p2 < len(right):
            # 左边大于右边的时候
            if left[p1] > 2 * right[p2]:
                # 左边后面所有的数都符合要求，因为是有序的数组
                self.pairs += len(left) - p1
                p2 += 1
            # 左边小于右边的时候，移动左边继续找，不再需要移动右边因为右边也是有序递增的数组
            else:
                p1 += 1

        # 再进行合并数组
        result = []
        while left and right:
            # 对比两个数组的第一个元素
            # 小的数字弹出并放进去结果数组
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # 如果左边还有数字，一定是有序的直接加到结果后面
        if left:
            result.extend(left)
        # 同理右边
        if right:
            result.extend(right)

        # 返回合并后的结果
        return result

    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        # 找中间节点
        middle = len(nums) // 2
        # 左右递归，拿到合并成功的数组
        left = self.merge_sort(nums[: middle])
        right = self.merge_sort(nums[middle:])
        # 合并当前节点的左右子树数组
        sub = self.merge_count(left, right)

        return sub

    def reversePairs(self, nums: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        这次我们利用归并排序的优势，每次对比的是两个有序数组，这样只有左边数组的出现满足条件的pairs时候，左边数组后面所有的数都可以和当前右边
        数组数构成合理的pairs。不需要遍历两个数组所有数。
        """
        sorted_nums = self.merge_sort(nums)

        return self.pairs


class SegTreeNode:
    def __init__(self, left=-1, right=-1, val=0, lazy_tag=None, left_node=None, right_node=None):
        self.left = left  # 区间左边界
        self.right = right  # 区间右边界
        self.mid = left + (right - left) // 2  # 区间中间点
        self.left_node = left_node  # 区间左节点
        self.right_node = right_node  # 区间右节点
        self.val = val  # 节点值（区间值）
        self.lazy_tag = lazy_tag  # 区间问题的延迟更新标记


# 动态开点线段树类，不带延迟更新标记的版本
class SegmentTree:
    # 初始化线段树接口
    def __init__(self, function):
        self.tree = SegTreeNode(-2 ** 31, 2 ** 31 - 1)
        self.function = function  # function 是一个函数，左右区间的聚合方法

    # 单点更新，将 nums[i] 更改为 val
    def update_point(self, i, val):
        self._update_point(i, val, self.tree)

    # 区间查询，查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self._query_interval(q_left, q_right, self.tree)

    # 以下为内部实现方法
    # 单点更新，将 nums[i] 更改为 val。node 节点的区间为 [node.left, node.right]
    def _update_point(self, i, val, node):
        if node.left == node.right:
            node.val += val  # 叶子节点，节点值修改为 val
            return

        if i <= node.mid:  # 在左子树中更新节点值
            if node.left_node is None:
                node.left_node = SegTreeNode(node.left, node.mid)
            self._update_point(i, val, node.left_node)
        else:  # 在右子树中更新节点值
            if node.right_node is None:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
            self._update_point(i, val, node.right_node)
        self._push_up(node)  # 向上更新节点的区间值

    # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def _query_interval(self, q_left, q_right, node):
        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            return node.val  # 直接返回节点值
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0

        res_left = 0  # 左子树查询结果
        res_right = 0  # 右子树查询结果
        if q_left <= node.mid:  # 在左子树中查询
            if node.left_node is None:
                node.left_node = SegTreeNode(node.left, node.mid)
            res_left = self._query_interval(q_left, q_right, node.left_node)
        if q_right > node.mid:  # 在右子树中查询
            if node.right_node is None:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
            res_right = self._query_interval(q_left, q_right, node.right_node)
        return self.function(res_left, res_right)  # 返回左右子树元素值的聚合计算结果

    # 向上更新 node 节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
    def _push_up(self, node):
        # 注意这里没有延迟标记的写法
        left_node = node.left_node
        right_node = node.right_node
        # 动态开点，遇到不存在的节点，直接赋值0
        left_node_val = left_node.val if left_node else 0
        right_node_val = right_node.val if right_node else 0

        node.val = self.function(left_node_val, right_node_val)


class Solution3:
    def reversePairs(self, nums: List[int]) -> int:
        """
        Time O(n * log(c))  c -> 线段树根节点维护的区间长度
        Space O(n * log(c))
        此题可以转化成线段树的思路，此题和327，315一模一样的思路，属于区间计数问题。
        我们可以从前往后遍历，把当前数字当成我们遍历到j的时候，我们需要找到遍历过的i，一定要符合
        2 * nums[j] < nums[i]，i < j 这个不等式，也就是说我们需要找到有多少个遍历过的数大于两倍的当前数，
        对此我们可以利用线段数RQS的方式，对一个区间快速的提取结果，需要注意的是这里的数可能很大，所以我们采用动态开点线段树，
        离散化存储，不需要开一个会超memory的连续数组。详细见注释。
        """
        upper_bound = 2 ** 32 - 1
        lower_bound = -2 ** 31
        # 初始化线段数，这里写的是动态开点线段树不带延迟标记的版本，区间的长度为题目给的最大范围
        segment_tree = SegmentTree(lambda x, y: x + y)
        res = 0

        for val in nums:
            # 需要查询的下限
            threshold = val * 2
            # 注意这里要先查询，再更新，因为自己不能算在里面，我们需要的是 i < j 对应的index
            res += segment_tree.query_interval(threshold + 1, upper_bound)
            # 更新的时候注意加入的数字大小，不能超过限制
            if lower_bound <= val <= upper_bound:
                # 更新当前数对应的线段数内的index的值
                segment_tree.update_point(val, 1)

        return res


s1 = Solution3()
print(s1.reversePairs(nums=[1, 3, 2, 3, 1]))
s2 = Solution2()
print(s2.reversePairs(nums=[2, 4, 3, 5, 1]))
