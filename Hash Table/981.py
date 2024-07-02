from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Space O(n)
        n is number of key, value pairs in hash map
        此题核心思想是利用加进来的数据是随着时间timestamp递增的，所以我们可以对每个key构建一个数组，数组里面是根据timestamp递增的时间点和
        value的pair，这样搜的时候直接二分法单调区间，找target值，左边界写法。set的时候直接append进去。
        """
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Time O(1)
        直接append进对应的key的list，append是O(1)的操作
        """
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Time O(log(n))
        n is number of pairs inside that key
        标准二分法左边界写法，这里找到target值后可以直接返回结果根据题意。如果没有target值的话，出循环后右指针的位置对应的是最大的接近
        target值的位置。
        """
        # 拿到对应的所有pairs
        values = self.hash_map[key]

        left = 0
        right = len(values) - 1
        # 左边界写法
        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][0] < timestamp:
                left = mid + 1
            elif values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                right = mid - 1

        # 特殊情况，如果小于0，说明越界没有对应的值
        if right < 0:
            return ""
        # 返回右指针位置的值
        else:
            return values[right][1]


obj = TimeMap()
obj.set(key="foo", value="bar", timestamp=1)
print(obj.get(key="foo", timestamp=1))
print(obj.get(key="foo", timestamp=3))
obj.set(key="foo", value="bar2", timestamp=4)
print(obj.get(key="foo", timestamp=4))
print(obj.get(key="foo", timestamp=5))
