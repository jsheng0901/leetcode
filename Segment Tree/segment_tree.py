# 线段树的节点类
class TreeNode:
    def __init__(self, val=0):
        self.left = -1  # 区间左边界
        self.right = -1  # 区间右边界
        self.val = val  # 节点值（区间值）
        self.lazy_tag = None  # 区间和问题的延迟更新标记


# 线段树类
class SegmentTreeArray:
    def __init__(self, nums, function):
        # 整个线段树，构造的时候需要遍历所有区间单点，单点更新的时候其实是二叉搜索树，二分发的思路，时间上是 O(log(n)) 的复杂度，
        # 区间更新和区间查询利用延迟标记，达到平均下来也都是 O(log(n) 的时间复杂度。
        # 如果只有单点更新加区间查询，带不带延迟标记都一样，因为区间查询和区间更新才是配套使用延迟标记的组合，达到降低时间复杂度的效果。
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
            self.__build(0, 0, self.size - 1)

    def __build(self, index, left, right):
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
        self.__build(left_index, left, mid)
        # 递归创建右子树
        self.__build(right_index, mid + 1, right)
        # 向上更新节点的区间值，此处相当于是后续遍历更新当前节点区间值
        self.__push_up(index)

        return

    def __push_up(self, index):
        # 向上更新下标为 index 的节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果，只更新当前节点
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
        self.__update_point(i, val, 0, 0, self.size - 1)

    def __update_point(self, i, val, index, left, right):
        # 单点更新，将 nums[i] 更改为 val。节点的存储下标为 index，节点的区间为 [left, right]
        # 单点更新和区间更新不一样得地方在于，单点更新不需要push down，不需要查看延迟标记，更新完叶子结点后，每一层都会通过push up，
        # 向上更新，来实现当前节点也就是父节点的更新
        # 当前节点
        node = self.tree[index]

        # 如果是叶子节点，则更新该节点的值
        if node.left == node.right:
            # 叶子节点，节点值修改为 val
            node.val = val
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
            self.__update_point(i, val, left_index, left, mid)
        # 在右子树中更新节点值
        else:
            self.__update_point(i, val, right_index, mid + 1, right)
        # 向上更新节点的区间值，类似构建的过程
        self.__push_up(index)

    def query_interval(self, q_left, q_right):
        # 区间查询，查询区间为 [q_left, q_right] 的区间值
        return self.__query_interval(q_left, q_right, 0, 0, self.size - 1)

    def __query_interval(self, q_left, q_right, index, left, right):
        # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值

        # 节点所在区间被 [q_left, q_right] 完全覆盖
        if left >= q_left and right <= q_right:
            # 直接返回节点值
            return self.tree[index].val
        # 节点所在区间与 [q_left, q_right] 无关，节点完全在查询区间外，一定要有这个返回值，为后续遍历位置左右返回值聚合函数使用
        if right < q_left or left > q_right:
            return 0

        # 向下更新当前节点的子节点，同理 update interval 的逻辑
        self.__push_down(index)

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
            res_left = self.__query_interval(q_left, q_right, left_index, left, mid)
        # 在右子树中查询
        if q_right > mid:
            res_right = self.__query_interval(q_left, q_right, right_index, mid + 1, right)

        # 返回左右子树元素值的聚合计算结果
        return self.function(res_left, res_right)

    def update_interval(self, q_left, q_right, val):
        # 区间更新，将区间为 [q_left, q_right] 上的元素值修改为 val，注意这里并不是增减 val，而是直接把区间内所有元素改成 val 值
        self.__update_interval(q_left, q_right, val, 0, 0, self.size - 1)

    def __update_interval(self, q_left, q_right, val, index, left, right):
        # 区间更新，需要用到延迟更新来保证每次区间查询和更新都是 O(log(n)) 级别的操作，否则更新区间可能是 O(n) 的操作
        # 延迟标记的意义是，该区间曾经被修改为 val，但其子节点区间值尚未更新
        # 在进行区间更新时，将区间子节点的更新操作延迟到，在后续操作中递归进入子节点时再执行，比如 query interval 的操作。
        # 这样一来，每次区间更新和区间查询的时间复杂度都降低到了 O(log(n))

        node = self.tree[index]
        # 节点所在区间被 [q_left, q_right] 完全覆盖
        if left >= q_left and right <= q_right:
            # 当前节点所在区间大小
            interval_size = (right - left + 1)
            # 当前节点所在区间每个元素值改为 val
            node.val = interval_size * val
            # 因为我们已经找到被完全覆盖要更新的区间，但此时当前节点对应的子节点还没有更新，
            # 将当前节点的延迟标记为区间值，后续再遇到当前节点的时候比如 query interval 的操作，会再次向下更新子节点的值
            node.lazy_tag = val
            return
        # 节点所在区间与 [q_left, q_right] 无关，直接结束
        if right < q_left or left > q_right:
            return

        # 向下更新当前节点的子节点
        self.__push_down(index)

        # 左右节点划分点
        mid = left + (right - left) // 2
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2
        # 在左子树中更新区间值
        if q_left <= mid:
            self.__update_interval(q_left, q_right, val, left_index, left, mid)
        # 在右子树中更新区间值
        if q_right > mid:
            self.__update_interval(q_left, q_right, val, right_index, mid + 1, right)

        # 向上更新当前节点的值，无论前面是否向下更新了子节点的值，都需要重新更新一次当前节点的值，和 update point 逻辑一样。
        self.__push_up(index)

    def __push_down(self, index):
        # 向下更新下标为 index 的节点所在区间的左右子节点的值和懒惰标记，当我们在查询此区间或者更新区间的时候才会进行这个操作
        # 在向下更新的时候，其实我们只更新当前节点的左右子节点的值，
        # 当前节点的值，在update interval的时候结束当前节点的时候，向上更新会更新当前节点的值

        # 先判断一下当前节点是否被标记过，如果没有被标记过说明并没有更新到此区间，直接跳过
        node = self.tree[index]
        lazy_tag = node.lazy_tag
        if lazy_tag is None:
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
        # 更新左子节点值，比如val是3，左子树的控制的区间长度为3，那么我们更新左子树值应该是控制区间内每个元素都会 +3，也就是长度 * val
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

    # 区间更新，将区间为 [q_left, q_right] 上的元素值增加 val
    def update_interval_add(self, q_left, q_right, val):
        # 区间更新，将区间为 [q_left, q_right] 上的元素值增加 val的版本
        self.__update_interval_add(q_left, q_right, val, 0, 0, self.size - 1)

    # 区间更新
    def __update_interval_add(self, q_left, q_right, val, index, left, right):
        node = self.tree[index]
        if left >= q_left and right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            if node.lazy_tag:
                node.lazy_tag += val  # 将当前节点的延迟标记增加 val
            else:
                node.lazy_tag = val  # 将当前节点的延迟标记增加 val
            interval_size = (right - left + 1)  # 当前节点所在区间大小
            node.val += val * interval_size  # 当前节点所在区间每个元素值增加 val
            return
        if right < q_left or left > q_right:  # 节点所在区间与 [q_left, q_right] 无关，直接结束
            return

        self.__push_down_add(index)

        mid = left + (right - left) // 2  # 左右节点划分点
        left_index = index * 2 + 1  # 左子节点的存储下标
        right_index = index * 2 + 2  # 右子节点的存储下标

        if q_left <= mid:  # 在左子树中更新区间值
            self.__update_interval_add(q_left, q_right, val, left_index, left, mid)
        if q_right > mid:  # 在右子树中更新区间值
            self.__update_interval_add(q_left, q_right, val, right_index, mid + 1, right)

        self.__push_up(index)

    # 向下更新下标为 index 的节点所在区间的左右子节点的值和懒惰标记
    def __push_down_add(self, index):
        # 先判断一下当前节点是否被标记过，如果没有被标记过说明并没有更新到此区间，直接跳过
        node = self.tree[index]
        lazy_tag = node.lazy_tag
        if lazy_tag is None:
            return

        left_index = index * 2 + 1  # 左子节点的存储下标
        right_index = index * 2 + 2  # 右子节点的存储下标

        left_node = self.tree[left_index]
        if left_node.lazy_tag:
            left_node.lazy_tag += lazy_tag  # 更新左子节点懒惰标记
        else:
            left_node.lazy_tag = lazy_tag
        left_size = (left_node.right - left_node.left + 1)
        left_node.val += lazy_tag * left_size  # 左子节点每个元素值增加 lazy_tag

        right_node = self.tree[right_index]
        if right_node.lazy_tag:
            right_node.lazy_tag += lazy_tag  # 更新右子节点懒惰标记
        else:
            right_node.lazy_tag = lazy_tag
        right_size = (right_node.right - right_node.left + 1)
        right_node.val += lazy_tag * right_size  # 右子节点每个元素值增加 lazy_tag

        node.lazy_tag = None  # 更新当前节点的懒惰标记


# 动态开点线段树的节点类
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

    # 单点更新，将 nums[i] 更改为 val
    def update_point(self, i, val):
        self.__update_point(i, val, self.tree)

    # 单点更新，将 nums[i] 更改为 val。node 节点的区间为 [node.left, node.right]
    def __update_point(self, i, val, node):
        # 叶子节点，节点值修改为 val
        if node.left == node.right:
            node.val = val
            return

        # 在左子树中更新节点值
        if i <= node.mid:
            # 如果左节点还没有构造，先构造左节点
            if node.left_node is None:
                node.left_node = SegTreeNode(node.left, node.mid)
            self.__update_point(i, val, node.left_node)
        # 在右子树中更新节点值
        else:
            # 如果右节点还没有构造，先构造右节点
            if node.right_node is None:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
            self.__update_point(i, val, node.right_node)
        # 向上更新节点的区间值
        self.__push_up(node)

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

    # 区间更新，将区间为 [q_left, q_right] 上的元素值增减 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)

    # 区间更新
    def __update_interval(self, q_left, q_right, val, node):
        # 节点所在区间被 [q_left, q_right] 所覆盖
        if node.left >= q_left and node.right <= q_right:
            # 如果有延迟标记
            if node.lazy_tag:
                # 将当前节点的延迟标记增加 val
                node.lazy_tag += val
            # 如果没有延迟标记
            else:
                # 将当前节点的延迟标记赋值为 val
                node.lazy_tag = val
            # 当前节点所在区间大小
            interval_size = (node.right - node.left + 1)
            # 当前节点所在区间每个元素值增加 val
            node.val += val * interval_size
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

        # 如果当前节点左节点存在延迟标记
        if node.left_node.lazy_tag:
            # 更新左子节点懒惰标记，这里是增减的 val的版本
            node.left_node.lazy_tag += lazy_tag  # 更新左子节点懒惰标记
        # 如果当前节点左节点不存在延迟标记
        else:
            # 更新左子节点懒惰标记，直接赋值
            node.left_node.lazy_tag = lazy_tag
        left_size = (node.left_node.right - node.left_node.left + 1)
        # 左子节点每个元素值增加 lazy_tag
        node.left_node.val += lazy_tag * left_size

        # 如果当前节点右节点存在延迟标记
        if node.right_node.lazy_tag:
            #  更新右子节点懒惰标记，这里是增减的 val 的版本
            node.right_node.lazy_tag += lazy_tag
        # 如果当前节点右节点不存在延迟标记
        else:
            # 更新右子节点懒惰标记，直接赋值
            node.right_node.lazy_tag = lazy_tag
        right_size = (node.right_node.right - node.right_node.left + 1)
        # 右子节点每个元素值增加 lazy_tag
        node.right_node.val += lazy_tag * right_size
        # 更新当前节点的懒惰标记
        node.lazy_tag = None
