from typing import List


class SegTreeNode:
    def __init__(self, left=-1, right=-1, val=0, lazy_tag=None, left_node=None, right_node=None):
        self.left = left  # 区间左边界
        self.right = right  # 区间右边界
        self.mid = left + (right - left) // 2  # 区间中间点
        self.left_node = left_node  # 区间左节点
        self.right_node = right_node  # 区间右节点
        self.val = val  # 节点值（区间值）
        self.lazy_tag = lazy_tag  # 区间问题的延迟更新标记


# 动态开点线段树类
class SegmentTree:
    def __init__(self, function):
        # 动态开点线段树，开始时只建立一个根节点，代表整个区间。
        # 当需要访问线段树的某棵子树（某个子区间）时，再建立代表这个子区间的节点。
        # 动态开点和非动态的线段树，核心思路思路是一模一样的，只是每次要对左右节点做操作的时候，先提前判断一下左右节点是否存在，
        # 如果不存在我们先构建左右节点，如果存在则继续操作。
        # 建立根节点
        self.tree = SegTreeNode(0, int(1e9))
        # function 是一个函数，左右区间的聚合方法
        self.function = function

    # 向上更新 node 节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
    def __push_up(self, node):
        left_node = node.left_node
        right_node = node.right_node
        # 需要查看左右节点是否存在，动态开点的前提是左右节点都已经构造过，但是这里的写法存疑
        # 应该是三种情况都要覆盖掉，否则子节点更新完成值后，父节点如果不是左右都存在的情况下，是不会更新父节点的值的，
        # 这样以来 query interval 的时候，如果interval是父节点的区间，会导致取值的结果是没有更新前的结果，而不是子节点更新过的结果。

        # 情况1：左右节点都存在，父节点是左右节点聚合之后结果
        if left_node and right_node:
            node.val = self.function(left_node.val, right_node.val)
        # 情况2：左节点存在，父节点是左结果更新之后的结果
        elif left_node:
            node.val = left_node.val
        # 情况3：右节点存在，父节点是右结果更新之后的结果
        elif right_node:
            node.val = right_node.val

    # 区间查询，查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, self.tree)

    # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, node):
        # 节点所在区间被 [q_left, q_right] 所覆盖
        if node.left >= q_left and node.right <= q_right:
            # 直接返回节点值
            return node.val
        # 节点所在区间与 [q_left, q_right] 无关
        if node.right < q_left or node.left > q_right:
            return 0

        # 向下更新节点所在区间的左右子节点的值和懒惰标记
        self.__push_down(node)

        # 左子树查询结果
        res_left = 0
        # 右子树查询结果
        res_right = 0

        # 在左子树中查询
        if q_left <= node.mid:
            # 同理单点更新，如果左节点还没有构造，先构造左节点
            if not node.left_node:
                node.left_node = SegTreeNode(node.left, node.mid)
            res_left = self.__query_interval(q_left, q_right, node.left_node)
        # 在右子树中查询
        if q_right > node.mid:
            # 同理单点更新，如果右节点还没有构造，先构造右节点
            if not node.right_node:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
            res_right = self.__query_interval(q_left, q_right, node.right_node)

        # 返回左右子树元素值的聚合计算结果
        return self.function(res_left, res_right)

    # 区间更新，将区间为 [q_left, q_right] 整体赋值为 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)

    # 区间更新
    def __update_interval(self, q_left, q_right, val, node):
        # 节点所在区间被 [q_left, q_right] 所覆盖
        if node.left >= q_left and node.right <= q_right:
            # 将当前节点的延迟标记赋值为 val
            node.lazy_tag = val
            # 这里不需要计算当前区间大小，因为此题区间更新的时候是直接把这整个区间更新成一个值，而不是对每个子区间内的叶子结点更新，
            # 也不需要对当前区间聚合所有子区间的结果
            # interval_size = (node.right - node.left + 1)
            # 当前节点所在区间整体赋值为 val
            # node.val += val * interval_size
            node.val = val
            return
        # 节点所在区间与 [q_left, q_right] 无关
        if node.right < q_left or node.left > q_right:
            return

        # 向下更新节点所在区间的左右子节点的值和懒惰标记
        self.__push_down(node)

        # 在左子树中更新区间值
        if q_left <= node.mid:
            # 同理单点更新，如果左节点还没有构造，先构造左节点
            if not node.left_node:
                node.left_node = SegTreeNode(node.left, node.mid)
            self.__update_interval(q_left, q_right, val, node.left_node)
        # 在右子树中更新区间值
        if q_right > node.mid:
            # 同理单点更新，如果右节点还没有构造，先构造右节点
            if not node.right_node:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
            self.__update_interval(q_left, q_right, val, node.right_node)

        # 向上更新当前节点的值
        self.__push_up(node)

    # 向下更新 node 节点所在区间的左右子节点的值和懒惰标记
    def __push_down(self, node):
        # 先判断一下当前节点是否被标记过，如果没有被标记过说明并没有更新到此区间，直接跳过
        lazy_tag = node.lazy_tag
        if not node.lazy_tag:
            return

        # 同理单点更新，如果左节点还没有构造，先构造左节点
        if not node.left_node:
            node.left_node = SegTreeNode(node.left, node.mid)
        # 同理单点更新，如果右节点还没有构造，先构造右节点
        if not node.right_node:
            node.right_node = SegTreeNode(node.mid + 1, node.right)

        # 更新左子节点懒惰标记，直接整体区间赋值，同理区间更新
        node.left_node.lazy_tag = lazy_tag
        # 左子节点每个整体区间赋值为 lazy_tag，同理区间更新
        node.left_node.val = lazy_tag

        # 更新右子节点懒惰标记，直接整体区间赋值，同理区间更新
        node.right_node.lazy_tag = lazy_tag
        # 右子节点每个整体区间赋值为 lazy_tag，同理区间更新
        node.right_node.val = lazy_tag
        # 更新当前节点的懒惰标记
        node.lazy_tag = None


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(n)
        此题使用动态开点线段树辅助，但是此题有一点不一样的是，当我们更新的时候，只要有交集区间，实际上是把整个有交集的区间的并集范围，进行更新。
        而不是只更新交集的部分，类似俄罗斯方块的逻辑。同样每次我们记录的是当前全局最高高度，而不是更新区间的最高高度。
        """
        # 构造线段树，聚合函数取最大值，因为query的时候我们需要取当前区间内最高点
        segment_tree = SegmentTree(lambda x, y: max(x, y))
        res = []
        # 记录当前全局最高点
        max_height = 0
        for position in positions:
            left, size = position[0], position[1]
            # 当前区间右端点，这里 -1，是因为有可能出现同一个点两个方块落下的情况，但是我们并不需要累加高度，允许平行的方块存在
            right = left + size - 1
            # 得到当前区间内最高点的高度，如果区间没有任何方块，高度将为0
            cur_height = segment_tree.query_interval(left, right)
            # 累加新的高度为此区间更新后的高度
            new_height = cur_height + size
            # 更新此区间为当前新高度
            segment_tree.update_interval(left, right, new_height)
            # 记录当前全局最高高度
            max_height = max(max_height, new_height)
            # 记录进结果
            res.append(max_height)

        return res


s = Solution()
print(s.fallingSquares(positions=[[1, 2], [2, 3], [6, 1]]))
print(s.fallingSquares(positions=[[100, 100], [200, 100]]))
