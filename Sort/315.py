from typing import List


class Solution1:
    def __init__(self):
        self.res = []

    def merge(self, left, right):
        # 先找出来当前左边数字有多少个右边数字比它小
        p1 = len(left) - 1
        p2 = len(right) - 1
        # 用从后向前的遍历思路，因为如果当前数字比右边的有序数组最大的还大的话，我们就不需要继续遍历右边剩下的部分
        while p1 >= 0 and p2 >= 0:
            left_num, left_index = left[p1][0], left[p1][1]
            right_num, right_index = right[p2][0], right[p2][1]
            # 左边大于右边的时候
            if left_num > right_num:
                # 右边前面所有的数都符合要求，因为是有序的数组
                self.res[left_index] += p2 + 1
                p1 -= 1
            # 左边小于右边的时候，移动左边继续找，不再需要移动右边因为右边也是有序递增的数组
            else:
                p2 -= 1

        # 再进行合并数组
        result = []
        while left and right:
            # 对比两个数组的第一个元素
            # 小的数字弹出并放进去结果数组
            if left[0][0] <= right[0][0]:
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
        if len(nums) <= 1:
            return nums
        # 找中间节点
        mid = len(nums) // 2
        # 左右递归，拿到合并成功的数组
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        # 合并当前节点的左右子树数组
        sub = self.merge(left, right)

        return sub

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(n)
        归并排序的思路，在进行merge的时候先算出多少个右边的数比当前左边的数少。这里思路同493。合并的时候其实需要遍历两次数组，其实会变慢。
        """
        # 先把index拿出来组合在一起，这样方便后续找到result数组位置
        nums_with_index = []
        for i, v in enumerate(nums):
            nums_with_index.append((v, i))

        self.res = [0] * len(nums)
        result = self.merge_sort(nums_with_index)

        return self.res


class Solution2:
    def __init__(self):
        self.res = []

    def merge(self, left, right):

        p1 = 0
        p2 = 0
        # 存储合并后结果的数组
        result = []
        while p1 < len(left) and p2 < len(right):
            left_num, left_index = left[p1][0], left[p1][1]
            right_num, right_index = right[p2][0], right[p2][1]
            # 左边小于等于右边的时候，此时说明右边前面的所有数都小于左边当前数，因为是递增数组
            if left_num <= right_num:
                # 加入合并的结果
                result.append(left[p1])
                # 右边前面所有的数都符合要求，因为是有序的数组
                self.res[left_index] += p2
                # 移动左指针
                p1 += 1
            # 左边大于右边的时候，移动右边继续找，不再需要移动左边因为左边也是有序递增的数组
            else:
                # 加入合并的结果
                result.append(right[p2])
                # 移动右指针
                p2 += 1

        # 左边还有没走完的数，此时后面所有数都比当前所有右边数组每个数都大
        while p1 < len(left):
            result.append(left[p1])
            # 同理更新结果
            self.res[left[p1][1]] += len(right)
            p1 += 1
        # 同理右边
        while p2 < len(right):
            result.append(right[p2])
            p2 += 1

        # 返回合并后的结果
        return result

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        sub = self.merge(left, right)

        return sub

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(n)
        归并排序的思路，同思路1，但是其实我们并不需要单调分开计算个数和合并数组。可以合在一起计算。这样更快对比思路1，详细见注释。
        """
        nums_with_index = []
        for i, v in enumerate(nums):
            nums_with_index.append((v, i))

        self.res = [0] * len(nums)
        result = self.merge_sort(nums_with_index)

        return self.res


class TreeNode:
    def __init__(self, val=0):
        self.left = -1  # 区间左边界
        self.right = -1  # 区间右边界
        self.val = val  # 节点值（区间值）
        self.lazy_tag = None  # 区间和问题的延迟更新标记


# 线段树类
class SegmentTree:
    def __init__(self, nums, function):
        # 树的大小
        self.size = len(nums)
        # 构建 TreeNode 数组，也就是线段树数组
        self.tree = [TreeNode() for _ in range(4 * self.size)]
        # 原始数据
        self.nums = nums
        # function 是一个函数，左右区间的聚合方法
        self.function = function

        # 构建树
        if self.size > 0:
            self._build(0, 0, self.size - 1)

    def _build(self, index, left, right):
        # 构建线段树，节点的存储下标为 index，节点的区间为 [left, right]，此处相当于是前序遍历构建树
        node = self.tree[index]
        node.left = left
        node.right = right

        # 叶子节点，节点值为对应位置的元素值
        if left == right:
            node.val = self.nums[left]
            return

        # 左右节点划分点，分裂点
        mid = left + (right - left) // 2
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2

        # 递归创建左子树
        self._build(left_index, left, mid)
        # 递归创建右子树
        self._build(right_index, mid + 1, right)
        # 向上更新节点的区间值，此处相当于是后续遍历更新当前节点区间值
        self._push_up(index)

        return

    def _push_up(self, index):
        # 向上更新下标为 index 的节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2
        # 当前树节点
        node = self.tree[index]
        left_node = self.tree[left_index]
        right_node = self.tree[right_index]
        # 赋值
        node.val = self.function(left_node.val, right_node.val)

    def update_point(self, i, val):
        # 单点更新，将 nums[i] 更改为 val
        self.nums[i] = val
        self._update_point(i, val, 0, 0, self.size - 1)

    def _update_point(self, i, val, index, left, right):
        # 单点更新，将 nums[i] 更改为 val。节点的存储下标为 index，节点的区间为 [left, right]

        # 当前节点
        node = self.tree[index]

        # 如果是叶子节点，则更新该节点的值
        if node.left == node.right:
            # 叶子节点，节点值修改为 val
            node.val += val
            return

        # 递归找到要更新的节点
        # 左右节点划分点
        mid = left + (right - left) // 2
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2

        # 在左子树中更新节点值
        if i <= mid:
            self._update_point(i, val, left_index, left, mid)
        # 在右子树中更新节点值
        else:
            self._update_point(i, val, right_index, mid + 1, right)
        # 向上更新节点的区间值，类似构建的过程
        self._push_up(index)

    def query_interval(self, q_left, q_right):
        # 区间查询，查询区间为 [q_left, q_right] 的区间值
        return self._query_interval(q_left, q_right, 0, 0, self.size - 1)

    def _query_interval(self, q_left, q_right, index, left, right):
        # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值

        # 节点所在区间被 [q_left, q_right] 完全覆盖
        if left >= q_left and right <= q_right:
            # 直接返回节点值
            return self.tree[index].val
        # 节点所在区间与 [q_left, q_right] 无关，节点完全在查询区间外
        if right < q_left or left > q_right:
            return 0

        self._push_down(index)

        # 左右节点划分点
        mid = left + (right - left) // 2
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2

        # 左子树查询结果
        res_left = 0
        # 右子树查询结果
        res_right = 0
        # 在左子树中查询
        if q_left <= mid:
            res_left = self._query_interval(q_left, q_right, left_index, left, mid)
        # 在右子树中查询
        if q_right > mid:
            res_right = self._query_interval(q_left, q_right, right_index, mid + 1, right)

        # 返回左右子树元素值的聚合计算结果
        return self.function(res_left, res_right)

    def _push_down(self, index):
        # 向下更新下标为 index 的节点所在区间的左右子节点的值和懒惰标记，当我们在查询此区间的时候才会进行这个操作

        node = self.tree[index]
        lazy_tag = node.lazy_tag
        if not lazy_tag:
            return

        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2

        left_node = self.tree[left_index]
        # 更新左子节点懒惰标记
        left_node.lazy_tag = lazy_tag
        # 左子树区间长度
        left_size = (left_node.right - left_node.left + 1)
        # 更新左子节点值
        left_node.val = lazy_tag * left_size

        right_node = self.tree[right_index]
        # 更新右子节点懒惰标记
        right_node.lazy_tag = lazy_tag
        # 右子树区间长度
        right_size = (right_node.right - right_node.left + 1)
        # 更新右子节点值
        right_node.val = lazy_tag * right_size

        # 更新当前节点的懒惰标记
        node.lazy_tag = None


class Solution3:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Time O(n * log(m))  n-> 多少个数   m -> 线段树数组的范围
        Space O(4 * m)
        线段树的思路，计算一个数后面有多少个比它小数，我们可以统计在[-inf, num - 1]这个区间内有多少个数存在。这里就可以转化成RQS的问题来做。
        线段树需要做的就是从后往前统计更新当前数字对应的index在线段树里面的位置 +1。这里有个小技巧是，因为数字有负数，但是数字本身就是线段树
        数组内的index，所以不能有负数，我们可以整体平移每个数一个范围，根据题意是10^4。
        不过此思路其实很慢，因为当线段数空间太大的时候，log(m) 远大于 log(n)，也就是思路2的速度明显更快。
        """
        # 平移的距离
        offset = 10 ** 4
        # 总共多少个可能的数值在数组里面
        size = 2 * 10 ** 4 + 1
        # 构建线段数数组
        tree = [0] * size
        result = []

        # 初始化线段数
        segment_tree = SegmentTree(tree, lambda x, y: x + y)

        # 从后向前遍历数组，因为是找数字后面有多少个比它小的数
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            # 计算有多少个小的数
            smaller_count = segment_tree.query_interval(0, num + offset - 1)
            # 反过来叠加结果，保证输出顺序
            result = [smaller_count] + result
            # 更新当前数对应的线段数内的index的值
            segment_tree.update_point(num + offset, 1)

        return result


s1 = Solution3()
print(s1.countSmaller(nums=[5, 2, 6, 1]))
s2 = Solution3()
print(s2.countSmaller(nums=[1, 9, 7, 8, 5]))
s3 = Solution3()
print(s3.countSmaller(nums=[-1, -1]))
