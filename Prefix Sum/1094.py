from typing import List


class Difference:
    def __init__(self, nums: List[int]):
        """
        Time O(n)
        Space O(n)
        差分数组，差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减。
        """
        self.diff = [0] * len(nums)
        # 根据初始数组构造差分数组
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self, i: int, j: int, val: int) -> None:
        """
        Time O(1)
        Space O(1)
        给闭区间 [i, j] 增加 val（可以是负数）,
        只要花费 O(1) 的时间修改 diff 数组，就相当于给 nums 的整个区间做了修改。多次修改 diff，
        然后通过 diff 数组反推，即可得到 nums 修改后的结果。
        """
        self.diff[i] += val
        # 当 j+1 >= diff.length 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 val 了。
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        """
        Time O(n)
        Space O(n)
        返回结果数组
        """
        result = [0] * len(self.diff)
        # 根据差分数组构造结果数组
        result[0] = self.diff[0]
        for i in range(1, len(result)):
            result[i] = result[i - 1] + self.diff[i]

        return result


class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Time O(n)
        Space O(n)
        典型的差分数组的应用，trips里面存放的就是对区间[i, j]增加的value
        """
        # 构造数组，直接取最大长度构造
        nums = [0] * 1001
        # 构造差分数组
        df = Difference(nums)

        for trip in trips:
            # 这里j的下车的index，所以应该是对[i, j - 1]进行增加value
            value, i, j = trip[0], trip[1], trip[2] - 1
            df.increment(i, j, value)

        result = df.result()
        # 每一站也就是每个数都不能超过限载人数，如果超过说明不行，直接返回false
        for n in result:
            if n > capacity:
                return False

        return True


class Solution2:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Time O(n * log(n))
        Space O(n)
        我们需要的只是每一站的时候乘客的变化，如果超过容量则说明不行。
        """
        timestamp = []
        # 记录每一站的时候乘客的人数变化
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        # 从第一站开始
        timestamp.sort()

        # 记录总共人数变化
        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            # 如果超过总容量，说明不行
            if used_capacity > capacity:
                return False

        return True


s = Solution2()
print(s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))
print(s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))
