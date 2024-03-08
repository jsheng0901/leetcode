from typing import List


class Solution1:
    def __init__(self):
        self.permutations = []

    def backtracking(self, nums, path, used):
        # 47题模版
        if len(path) == len(nums):
            self.permutations.append(path[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False:
                continue

            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, path, used)
            used[i] = False
            used[i] = True
            self.backtracking(nums, path, used)
            used[i] = False
            path.pop()

        return

    def is_square(self, num):
        # 判断两两相邻的是不是square
        for i in range(len(num) - 1):
            total = num[i] + num[i + 1]
            if (total ** 0.5) % 1 != 0:
                return False

        return True

    def numSquarefulPerms(self, nums: List[int]) -> int:
        """
        Time O(n * log(n) + n! + n * n)
        Space O(n)
        基于47题的写法，先找出所有的组合，然后一一判断是不是square。很明显TLE。因为有时候前面的组合已经不是square了但是还在回溯构建组合。
        """
        # 查重的写法和47一样
        used = len(nums) * [False]
        nums.sort()
        self.backtracking(nums, [], used)
        # 开始扫描所有组合并判断
        result = 0
        for permutation in self.permutations:
            if self.is_square(permutation):
                result += 1

        return result


class Solution2:
    def __init__(self):
        self.result = 0

    def backtracking(self, nums, path, used):
        # 走到底，所有数字都已经使用了
        if len(path) == len(nums):
            # 可以走到这里说明前面的两两组合都是valid的square，结果 +1
            self.result += 1
            return

        for i in range(len(nums)):
            # 查重判断
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False:
                continue
            # 自己不能重复使用进组合
            if used[i]:
                continue
            # 当前加入的数
            path.append(nums[i])
            # 如果只有一个数，继续回溯
            if len(path) == 1:
                used[i] = True
                self.backtracking(nums, path, used)
                used[i] = False
            # 如果有两个数以上，判断是否是square，如果不是则不再继续这条递归路线
            if len(path) > 1 and (path[-2] + path[-1]) ** 0.5 % 1 == 0:
                used[i] = True
                self.backtracking(nums, path, used)
                used[i] = False
            path.pop()

        return

    def numSquarefulPerms(self, nums: List[int]) -> int:
        """
        Time O(n * log(n) + n!)
        Space O(n)
        思路和解法1一样，只是每次我们加入新的数进来的时候，判断一下和前一个数能不能构成square，如果可以再继续回溯构建组合。
        """
        used = len(nums) * [False]
        nums.sort()
        self.backtracking(nums, [], used)

        return self.result


s1 = Solution2()
print(s1.numSquarefulPerms(nums=[2, 2, 2]))
s2 = Solution2()
print(s2.numSquarefulPerms(nums=[1, 17, 8]))
