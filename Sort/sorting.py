from typing import List


class BubbleSort:
    def __init__(self):
        print('This is bubble sorting!')

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n^2) --> O(n)
        Space O(1)  -- in-place
        1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
        2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
        3. 针对所有的元素重复以上的步骤，除了最后一个。
        4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
        """
        # 对 arr 进行拷贝，不改变参数内容，正常可以in-place排序只是这里刻意这样写
        arr_copy = arr[:]

        # 这里 i 代表的是遍历整个array的次数
        for i in range(1, len(arr_copy)):
            # 设定一个标记，若为true，则表示此次循环没有进行交换，也就是待排序列已经有序，排序已经完成。
            flag = True
            # 从第一个到i预留的最后一位的地方进行对比，-1的目的是因为每次排完后最后一个一定已经是最大的数字了
            for j in range(len(arr_copy) - i):
                # 如果左边大于右边，进行swap
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    # 同时更新flag
                    flag = False

            # 如果为true，说明排完了
            if flag:
                break

        return arr_copy


class SelectSort:
    def __init__(self):
        print('This is select sorting!')

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n^2)
        Space O(1)  -- in-place
        1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
        2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        3. 重复第二步，直到所有元素均排序完毕。
        """
        # 对 arr 进行拷贝，不改变参数内容，正常可以in-place排序只是这里刻意这样写
        arr_copy = arr[:]

        # 总共要经过 N-1 轮比较，因为要对比每次要对比排完的index后面的所有元素
        for i in range(len(arr_copy) - 1):
            # 记录当前最小元素的初始index
            min_index = i
            # 每轮需要比较的次数 N-i，及对比i之后的所有元素的大小
            for j in range(i + 1, len(arr_copy)):
                # 找到更小的元素对比 min index 元素
                if arr_copy[j] < arr_copy[min_index]:
                    # 记录目前能找到的最小值元素的下标
                    min_index = j

            # 将找到的最小值和i位置所在的值进行交换
            if i != min_index:
                arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]

        return arr_copy


class InsertSort:
    def __init__(self):
        print('This is insert sorting!')

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n^2) --> O(n)
        Space O(1)  -- in-place
        1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
        2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
          （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
        """
        # 对 arr 进行拷贝，不改变参数内容，正常可以in-place排序只是这里刻意这样写
        arr_copy = arr[:]

        # 从下标为1的元素开始选择合适的位置插入，因为下标为0的只有一个元素，默认是有序的
        for i in range(1, len(arr_copy)):
            # 记录要插入的数据
            tmp = arr_copy[i]

            # 从已经排序的序列最右边的开始比较，找到比其小的数
            j = i
            while j > 0 and tmp < arr_copy[j - 1]:
                arr_copy[j], arr_copy[j - 1] = arr_copy[j - 1], arr_copy[j]
                j -= 1

            # 存在比其小的数，插入到当前小的数的前面一位index，因为上面对比的时候用的是 j - 1，说明此时 j - 1 > tmp 及要插入的数字
            if j != i:
                arr_copy[j] = tmp

        return arr_copy


class ShellSort:
    def __init__(self):
        print('This is shell sorting!')

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(1)  -- in-place
        1. 选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
        2. 按增量序列个数 k，对序列进行 k 趟排序；
        3. 每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。
           仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
        """
        # 对 arr 进行拷贝，不改变参数内容，正常可以in-place排序只是这里刻意这样写
        arr_copy = arr[:]
        # 对整个 array 先进行子序列，先计算出最大的gap
        gap = 1
        while gap < len(arr_copy):
            gap = gap * 3 + 1

        # 遍历整个序列gap，比如 gap = 4，1 ...
        while gap > 0:
            # 对每个子序列里面进行 insert sort
            for i in range(gap, len(arr_copy)):
                # 提取出当前要对比的数字
                tmp = arr_copy[i]
                # 需要对比的另一个数字的index
                j = i - gap
                # 如果此时左边index j 对应的数字大于要对比的数字，进行swap也就是 insert sort
                while j >= 0 and arr_copy[j] > tmp:
                    # swap
                    arr_copy[j], arr_copy[j + gap] = arr_copy[j + gap], arr_copy[j]
                    j -= gap
            # 递减增量 gap
            gap //= 3

        return arr_copy


class MergeSort:
    def __init__(self):
        print('This is merge sorting!')

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        # 合并后的数组
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

        return result

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(n)
        1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
        2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
        3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
        4. 重复步骤 3 直到某一指针达到序列尾；
        5. 将另一序列剩下的所有元素直接复制到合并序列尾。
        简单点说就是，本质上是分治的思路，分治是二叉树的思路，这里是后续遍历的思路。分裂到最小只有一个元素的时候直接返回，
        大于一个元素的数组进行左右两边合并，合并的原理就是取两个数组的头元素，那个小就先放进结果数组，一次放进去所有两个数组元素，
        之后通过后续遍历继续往上递归返回合并成功的数组，直到最后全部合并起来。
        """
        # 走到底，只有一个元素，直接返回
        if len(arr) < 2:
            return arr
        # 找中间节点
        middle = len(arr) // 2
        # 左右递归，拿到合并成功的数组
        left = self.sort(arr[: middle])
        right = self.sort(arr[middle:])
        # 合并当前节点的左右子树数组
        sub_res = self.merge(left, right)

        return sub_res


class QuickSort:
    def __init__(self):
        print('This is quick sorting!')

    def partition(self, arr: List[int], left: int, right: int) -> int:
        # 随机选择一个作为pivot指针，这里也可以用random.randint(left, right)
        pivot = left

        # 先把pivot指针对应的数放到最右边去
        arr[pivot], arr[right] = arr[right], arr[pivot]

        # store 指针用来找到大于pivot指针对应数的index
        store_index = left
        # 遍历数组
        for i in range(left, right):
            # 如果当前数字小于最右边的数字，也就是pivot指针数字
            if arr[i] < arr[right]:
                # 交换 store 指针对应的大于pivot指针的数字和当前数字，也就是把小于pivot的都移动到最右边去
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        # 最后store指针的位置就是当我们移动完所有小于pivot指针数字之后的下一个index也就是pivot应该移动回来的index
        arr[store_index], arr[right] = arr[right], arr[store_index]

        # 返回pivot指针数字排序完成后的index
        return store_index

    def quick_sort(self, arr: List[int], left: int, right: int) -> None:
        # 如果越界说明数组已经遍历结束
        if left >= right:
            return

        # 得到当前pivot指针排序完成后的位置，可以理解为树结构中的中间节点
        pivot = self.partition(arr, left, right)

        # 分别遍历pivot两边的数组，也就是树节点的左右子节点
        self.quick_sort(arr, left, pivot - 1)
        self.quick_sort(arr, pivot + 1, right)

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(log(n)) -- in-place
        1. 从数列中挑出一个元素，称为 “基准”（pivot）;
        2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
           在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
        3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
        总结来说，快速排序是一种分而治之思想在排序算法上的应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。
        只不过这个分治是从下到上的遍历，而不是merge sort用从下到上返回的形式。前者是树的前序遍历后者是树的后序遍历。
        """
        # 初始化左右指针
        left = 0
        right = len(arr) - 1
        # 快排
        self.quick_sort(arr, left, right)

        return arr


class HeapSort:
    def __init__(self):
        print('This is heap sorting!')

    def build_max_heap(self, arr: List[int]) -> None:
        length = len(arr)
        # 对每个节点构建大顶堆，除叶子结点
        for i in range(length // 2 - 1, -1, -1):
            self.heapify(arr, length, i)

    def heapify(self, arr: List[int], n: int, i: int) -> None:
        # 构建大顶堆算法
        # 初始化当前root index为最大值对应的index
        largest = i
        # 左右孩子节点的index
        left = 2 * i + 1
        right = 2 * i + 2

        # 如果左孩子更大，最大值对应的index赋值为左孩子
        if left < n and arr[left] > arr[largest]:
            largest = left

        # 如果右孩子更大，最大值对应的index赋值为右孩子
        if right < n and arr[right] > arr[largest]:
            largest = right

        # 如果当前root不是最大值对应的index，说明要进行swap，保证堆顶是最大值
        if largest != i:
            # swap两个index
            arr[i], arr[largest] = arr[largest], arr[i]
            # 继续递归原先最大值对于的index为root的子树
            self.heapify(arr, n, largest)

        return

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(log(n)) -- in-place，但是递归有占用space
        1. 创建一个大顶堆，保证数组最大的数在第一位堆顶。
        2. 此时我们知道最大的数一定在第一位，把最大的和最后一个数进行swap。
        3. 把堆的尺寸缩小 1，减掉最后一个最大的数，继续创建大顶堆。
        4. 重复 2 - 3 的步骤，直到堆只剩下一个数。
        """
        # 初始化构建大顶堆，第一步
        self.build_max_heap(arr)

        # 从后向前重新构建大顶堆，每次堆缩小一个数
        for i in range(len(arr) - 1, -1, -1):
            # 把堆顶最大值放到最后一位去
            arr[0], arr[i] = arr[i], arr[0]
            # 对剩下的堆继续重新调整大顶堆，保证堆顶是最大值
            self.heapify(arr, i, 0)

        return arr


class CountingSort:
    def __init__(self):
        print('This is counting sorting!')

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n + k)   n -> number of element  k -> number of element between min and max
        Space O(n)
        1. 统计所有数出现的频率
        2. 找到最大值和最小值
        3. 此时所有数出现的顺序应该在最大值和最小值中间
        4. 按照最大值最小值的范围，一个一个数找出来频率，然后放进按照新的index放进数组
        """
        counts = {}
        # 找出最大值最小值，确定存在的范围
        min_value, max_value = min(arr), max(arr)
        # 统计每个数出现的频率
        for val in arr:
            counts[val] = counts.get(val, 0) + 1

        # 新的index
        sorted_index = 0
        # 在范围内一个一个数遍历
        for val in range(min_value, max_value + 1):
            # 当这个数存在的时候，按照出现频率的次数放进结果
            while counts.get(val, 0) > 0:
                # 按新的index的位置放进结果
                arr[sorted_index] = val
                # 新的index +1
                sorted_index += 1
                # 更新频率
                counts[val] -= 1

        return arr


class BucketSort:
    def __init__(self):
        print('This is bucket sorting!')

    def bucket_sort(self, arr: List[int], bucket_size: int) -> List[int]:
        # 找到最大值最小值
        min_value, max_value = min(arr), max(arr)
        # 计算出桶的个数
        bucket_count = (max_value - min_value) // bucket_size + 1
        # 初始化所有桶
        buckets = [[] for _ in range(bucket_count)]

        # 把每个数放进桶内
        for i in range(len(arr)):
            # 计算属于哪个桶
            bucket_index = (arr[i] - min_value) // bucket_size
            # 如果没有数字在桶内
            # if buckets[bucket_index] is None:
            #     # 初始化当前桶
            #     buckets[bucket_index] = [arr[i]]
            # # 如果有数字在桶内
            # else:
            #     # 直接加进去
            buckets[bucket_index].append(arr[i])

        arr_index = 0
        # 遍历每个分桶
        for bucket in buckets:
            if len(bucket) <= 0:
                continue
            # 对每个分桶内进行排序
            bucket = InsertSort().sort(bucket)
            # 把排完序后的结果放进数组
            for val in bucket:
                arr[arr_index] = val
                arr_index += 1

        return arr

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(n + k) worse O(n^2)
        Space O(n)
        1. 基于基数排序的原理，先计算出有多少个桶
        2. 把每个数按照桶的大小放进不同的桶内
        3. 对每个桶内进行insert sort，插入排序，也可以是任意其它排序方式
        4. 把每个排序完的桶重新放回结果
        桶排序和奇数排序的原理基本一样，主要是利用数字分组的原理，非常不同的桶然后对每个桶内再进行排序，然后组合起来排序的结果。
        """
        return self.bucket_sort(arr, 5)


class RadixSort:
    def __init__(self):
        print('This is radix sorting!')

    def get_max_element(self, arr):
        # 找到数组中的最大值
        max_element = arr[0]
        for val in arr:
            max_element = max(abs(val), max_element)

        return max_element

    def get_max_digits(self, max_element):
        # 找到最大的位数
        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element = max_element // 10

        return max_digits

    def bucket_sort(self, arr, place_value):
        # 构建bucket
        buckets = [[] for _ in range(10)]
        # 对每个数进行分桶
        for val in arr:
            digit = abs(val) / place_value
            digit = int(digit % 10)
            # 把对应的数放进不同额桶
            buckets[digit].append(val)

        # 对每个桶每一位数重新放进数组
        index = 0
        for digit in range(10):
            for val in buckets[digit]:
                arr[index] = val
                index += 1

    def radix_sort(self, arr, max_digits):
        place_value = 1
        # 对每一位数进行分桶排序
        for _ in range(max_digits):
            self.bucket_sort(arr, place_value)
            place_value *= 10

        # 如果有负数需要把负数reverse一下，重新排在正数前面
        positives = [val for val in arr if val >= 0]
        negatives = [val for val in arr if val < 0]
        negatives.reverse()

        return negatives + positives

    def sort(self, arr: List[int]) -> List[int]:
        """
        Time O(d * (n + b))     d -> max digit number  n -> number of element  b -> number of bucket
        Space O(n + b)
        1. 先拿到最大的数，和最多多少位数
        2. 每个数字从个位开始到最大位，对每一位数，进行分桶排序
        3. 总共十个桶，对应每一位最多十个数，每个数字对应的位放进对应的桶，也就是按照对应的位数进行排序
        4. 把分完桶之后的数从新拿出来排序
        5. 重复 2 - 3 直到遍历完所有位
        """
        # 拿到最大值
        max_element = self.get_max_element(arr)
        # 拿到最大位数
        max_digits = self.get_max_digits(max_element)

        return self.radix_sort(arr, max_digits)


test_case = [2, 5, 4, 3, 8, 1, 10, 6, 9, 7]
print('----------------------------')
bubble_test = BubbleSort()
print(bubble_test.sort(test_case))
print('----------------------------')
select_test = SelectSort()
print(select_test.sort(test_case))
print('----------------------------')
insert_test = InsertSort()
print(insert_test.sort(test_case))
print('----------------------------')
shell_test = ShellSort()
print(shell_test.sort(test_case))
print('----------------------------')
merge_test = MergeSort()
print(merge_test.sort(test_case))
print('----------------------------')
quick_test = QuickSort()
print(quick_test.sort(test_case))
print('----------------------------')
heap_test = HeapSort()
print(heap_test.sort(test_case))
print('----------------------------')
counting_test = CountingSort()
print(counting_test.sort(test_case))
print('----------------------------')
bucket_test = BucketSort()
print(bucket_test.sort(test_case))
print('----------------------------')
radix_test = RadixSort()
print(radix_test.sort(test_case))
