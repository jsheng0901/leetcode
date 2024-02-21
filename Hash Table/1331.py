from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Time O(n * log(n) + 2 * n)
        Space O(n)
        先排序一遍，在遍历所有数字记录对应的index，这里需要注意的是如果前面一个数字和后面一个数组重复的话，直接跳过，同时跳过之后
        我们记录rank应该用前一个不一样的数字的rank + 1。
        """
        if len(arr) == 0:
            return arr

        sorted_array = sorted(arr)
        value_to_index = {sorted_array[0]: 1}

        for i, v in enumerate(sorted_array):
            # 如果是同样的数字则跳过，只保留最小的index
            if i > 0 and sorted_array[i] == sorted_array[i - 1]:
                continue
            # 这里是最需要注意的地方，新的rank应该是前一个不同的数字的rank + 1
            if i > 0 and v not in value_to_index:
                value_to_index[v] = value_to_index[sorted_array[i - 1]] + 1

        res = []
        for num in arr:
            res.append(value_to_index[num])

        return res


class Solution2:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Time O(n * log(n) + 2 * n)
        Space O(n)
        一模一样的做法，只是我们可以先用set筛选掉重复的数字，这样就不用担心记录的rank对不上了
        """
        rank = {}
        # 先筛选掉多余的重复的数字
        sorted_arr = sorted(set(arr))
        # 记录rank
        for i, v in enumerate(sorted_arr):
            rank[v] = i + 1

        res = []
        # 更新进结果
        for num in arr:
            res.append(rank[num])

        return res


s = Solution2()
print(s.arrayRankTransform(arr=[]))
print(s.arrayRankTransform(arr=[40, 10, 20, 30]))
print(s.arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]))
