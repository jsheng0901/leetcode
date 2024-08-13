from typing import List


class Solution1:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        Time O( n * log(n) + n^2) --> O(n^2)
        Space O(n)
        将所有矩形的左右边界按照横坐标进行排序，这样就确定了扫描线扫描的顺序。随后我们遍历这些左右边界，一次性地处理掉一批横坐标相同的左右边界，
        对应地增加或者减少覆盖的长度。在这之后，下一个未遍历到的左右边界的横坐标，减去这一批左右边界的横坐标，就是扫描线在水平方向移动过的距离。
        seg[i] 表示第 i 个线段被矩形覆盖的次数，length[i] 表示第 i 个线段的长度。
        当扫描线遇到一个左边界时，我们就将左边界覆盖到的线段对应的 seg[i] 全部加 1；
        遇到一个右边界时，我们就将右边界覆盖到的线段对应的 seg[i] 全部减 1。
        在处理掉一批横坐标相同的左右边界后，seg[i] 如果大于 0，说明它被覆盖，我们累加所有的 length[i]，即可得到「覆盖的线段长度」
        """
        mod = 10 ** 9 + 7
        # 记录所有Y轴的值
        y_bound = set()
        for rect in rectangles:
            # 下边界
            y_bound.add(rect[1])
            # 上边界
            y_bound.add(rect[3])

        # sort一遍Y轴的值，保证后续遍历的时候是从上到下的顺序
        y_bound = sorted(y_bound)
        m = len(y_bound)
        # 「思路与算法部分」的 length 数组并不需要显式地存储下来
        # length[i] 可以通过 y_bound[i+1] - y_bound[i] 得到
        # m 个水平线有 m - 1 个区间
        seg = [0] * (m - 1)

        sweep = list()
        for i, rect in enumerate(rectangles):
            # 左边界，这里用1来表示有矩形开始
            sweep.append((rect[0], i, 1))
            # 右边界，这里用-1来表示有矩形结束
            sweep.append((rect[2], i, -1))

        # 保证从左到右的顺序扫描一遍所有X轴上面的点
        sweep.sort()

        ans = i = 0
        # 从左到右开始遍历
        while i < len(sweep):
            j = i
            # 指针走到X轴上的点是一样的数值的index
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1
            # 走到最后一个不用再计算面积，直接结束
            if j + 1 == len(sweep):
                break

            # 一次性地处理掉一批横坐标相同的左右边界
            for k in range(i, j + 1):
                # 拿到当前点原始index和左右边界的状态
                _, idx, diff = sweep[k]
                # 拿到当前点对应在Y轴上的上下边界
                low, upper = rectangles[idx][1], rectangles[idx][3]
                # 遍历所有Y轴上的区间
                for y in range(m - 1):
                    # 如果刚好此区间在当前点的上下边界内，也就是说明此区间有矩形覆盖到
                    if low <= y_bound[y] and y_bound[y + 1] <= upper:
                        # 累计状态
                        seg[y] += diff

            # 开始计算覆盖到的高度
            cover = 0
            # 遍历所有Y轴上的区间
            for k in range(m - 1):
                # 如果大于0，以为的有覆盖
                if seg[k] > 0:
                    # 累计覆盖长度
                    cover += (y_bound[k + 1] - y_bound[k])

            # 最终面积为 Y轴上的覆盖长度 * X轴上扫描线在水平方向移动过的距离
            ans += cover * (sweep[j + 1][0] - sweep[j][0])
            # 指针跳到下一个X轴的值不一样的点
            i = j + 1

        return ans % mod


# 线段树的节点类
class SegTreeNode:
    def __init__(self, left=-1, right=-1, cnt=0, height=0, left_node=None, right_node=None):
        self.left = left  # 区间左边界
        self.right = right  # 区间右边界
        self.mid = left + (right - left) // 2
        self.left_node = left_node  # 区间左节点
        self.right_node = right_node  # 区间右节点
        self.cnt = cnt  # 节点值（区间值，当前区间备覆盖到的次数
        self.height = height  # 区间问题的延迟更新标记，同样是当前区间覆盖的距离


# 线段树类
class SegmentTree:
    # 初始化线段树接口
    def __init__(self):
        self.tree = SegTreeNode(0, int(1e9))

    # 区间更新接口：将区间为 [q_left, q_right] 上的元素值修改为 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)

    # 区间查询接口：查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, self.tree)

    # 以下为内部实现方法

    # 区间更新实现方法
    def __update_interval(self, q_left, q_right, val, node):

        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return

        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            node.cnt += val  # 当前节点所在区间每个元素值增加 val
            self.__push_up(node)
            return

        self.__push_down(node)

        if q_left <= node.mid:  # 在左子树中更新区间值
            self.__update_interval(q_left, q_right, val, node.left_node)
        if q_right > node.mid:  # 在右子树中更新区间值
            self.__update_interval(q_left, q_right, val, node.right_node)

        self.__push_up(node)

    # 区间查询实现方法：在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, node):
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0

        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            return node.height  # 直接返回节点值

        self.__push_down(node)

        res_left = 0  # 左子树查询结果
        res_right = 0  # 右子树查询结果
        if q_left <= node.mid:  # 在左子树中查询
            res_left = self.__query_interval(q_left, node.mid, node.left_node)
        if q_right > node.mid:  # 在右子树中查询
            res_right = self.__query_interval(node.mid + 1, q_right, node.right_node)

        return res_left + res_right  # 返回左右子树元素值的聚合计算结果

    # 向上更新实现方法：更新 node 节点区间值 等于 该节点左右子节点元素值的聚合计算结果
    def __push_up(self, node):
        # 如果当前节点有覆盖过
        if node.cnt > 0:
            # 更新当前节点的覆盖长度
            node.height = node.right - node.left + 1
        # 如果当前节点没有覆盖过
        else:
            # 聚合当前节点结果为子节点的和
            if node.left_node and node.right_node:
                node.height = node.left_node.height + node.right_node.height
            else:
                node.height = 0

    # 向下更新实现方法：更新 node 节点所在区间的左右子节点的值和懒惰标记
    def __push_down(self, node):
        if node.left_node is None:
            node.left_node = SegTreeNode(node.left, node.mid)
        if node.right_node is None:
            node.right_node = SegTreeNode(node.mid + 1, node.right)


class Solution2:
    def rectangleArea(self, rectangles) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        整体思路和思路1是一模一样的，这里也是按照从左到右遍历X轴上面的点，然后得到对应的Y轴被覆盖的长度，只是这里Y轴被覆盖的长度用线段树
        来实现，思路1里面的count计算被覆盖的次数和计算被覆盖的总长度
        """
        # lines 存储每个矩阵的上下两条边
        lines = []

        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            lines.append([x1, y1 + 1, y2, 1])
            lines.append([x2, y1 + 1, y2, -1])

        lines.sort(key=lambda line: line[0])

        # 建立线段树
        seg_tree = SegmentTree()

        ans = 0
        mod = 10 ** 9 + 7
        prev_x = lines[0][0]
        for i in range(len(lines)):
            x, y1, y2, val = lines[i]
            # 得到当前遍历的X轴的点上Y轴线段分布下，被覆盖的长度和
            height = seg_tree.query_interval(0, int(1e9))
            # 更新面积
            ans += height * (x - prev_x)
            # 更新当前X轴点对应的Y轴的覆盖情况
            seg_tree.update_interval(y1, y2, val)
            # 更新X轴的指针
            prev_x = x

        return ans % mod


s = Solution2()
print(s.rectangleArea(rectangles=[[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
print(s.rectangleArea(rectangles=[[0, 0, 1000000000, 1000000000]]))
print(s.rectangleArea(rectangles=[[0, 0, 1, 1], [2, 2, 3, 3]]))
print(s.rectangleArea(rectangles=[[0, 0, 2, 2], [1, 1, 3, 3]]))
