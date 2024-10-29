from collections import Counter, defaultdict
from typing import List


class Solution1:
    def dp(self, freq, memo):
        # 所有数字都用完了，返回0
        if all([v == 0 for v in freq.values()]):
            return 0

        # 序列化字典的作为key来存储，转化成tuple
        if tuple(sorted(freq.items())) in memo:
            return memo[tuple(sorted(freq.items()))]

        sub = 0
        for k, v in freq.items():
            # 因为不会删掉key，所以要判断一下是否还存在
            if v > 0:
                # 减少当前使用的数的频率
                freq[k] -= 1
                low = k - 1
                up = k + 1
                # 对于上一个数，进行删减
                if low in freq:
                    low_v = freq[low]
                    freq[low] = 0
                # 对于下一个数，进行删减
                if up in freq:
                    up_v = freq[up]
                    freq[up] = 0
                # 递归找最大返回值，记得叠加当前选择的数
                sub = max(sub, self.dp(freq, memo) + k)
                # 这里要回溯一下，因为下一个选择的数的时候，之前删除的要加回来
                if low in freq:
                    freq[low] = low_v
                if up in freq:
                    freq[up] = up_v
                freq[k] += 1

        # 存储进备忘录，同前面要转化成tuple
        memo[tuple(sorted(freq.items()))] = sub

        return sub

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Time O(n!)
        Space O(n!)
        最基础的暴力解法加备忘录DP的写法，备忘录记录的是当前数组选完要take的point后的频率字典。
        这里即使带了备忘录也是非常非常耗时的，明显TLE。因为出现的unique的数字的个数和频率组合，也就是所有数字的组合太多了。
        """
        freq = Counter(nums)
        memo = {}

        return self.dp(freq, memo)


class Solution2:
    def dp(self, nums, memo):
        if len(nums) == 0:
            return 0

        if tuple(nums) in memo:
            return memo[tuple(nums)]

        sub = 0
        for i in range(len(nums)):
            tmp = nums[:i] + nums[i+1:]
            new_num = []
            low = nums[i] - 1
            up = nums[i] + 1
            for val in tmp:
                if val != low and val != up:
                    new_num.append(val)
            sub = max(sub, self.dp(new_num, memo) + nums[i])

        memo[tuple(nums)] = sub

        return sub

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Time O(n!)
        Space O(n!)
        同思路1，只是换成数组来写，更慢，因为每次要重组新数组。
        """
        memo = {}

        return self.dp(nums, memo)


class Solution3:
    def dp(self, freq, memo):
        if all([v == 0 for v in freq.values()]):
            return 0

        if tuple(freq.items()) in memo:
            return memo[tuple(freq.items())]

        sub = 0
        for k, v in freq.items():
            if v > 0:
                # 区别在这里，直接拿掉所有出现的频率
                freq[k] = 0
                low = k - 1
                up = k + 1
                if low in freq:
                    low_v = freq[low]
                    freq[low] = 0
                if up in freq:
                    up_v = freq[up]
                    freq[up] = 0
                # 这里计算当前point的时候，直接记录所有出现的频率
                sub = max(sub, self.dp(freq, memo) + k * v)
                if low in freq:
                    freq[low] = low_v
                if up in freq:
                    freq[up] = up_v
                freq[k] = v

        memo[tuple(freq.items())] = sub

        return sub

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Time O((unique num)!)
        Space O((unique num)!)
        整体思路和思路1一样，只是每次拿掉一个数的时候，直接拿掉所有出现的频率而不是一次一次的删减，因为没区别最后计算point的时候。会快一点，
        因为只需要计算unique num次数的所有组合。但是还是很慢，TLE。
        """
        freq = Counter(nums)
        memo = {}

        return self.dp(freq, memo)


class Solution4:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Time O(n + k)
        Space O(n + k)
        其实仔细看这题和house robber一模一样，如果当前数被选的话，我们只能从当前数n-2来找最大值，如果没有被选，那么可以继续累计n-1的情况。
        这里并不需要考虑n+1的情况，因为后面一个数的最大值会走到后面的时候再重新计算两种情况。
        DP数组表示，dp[i]为选择当前数i的时候最大可以得到的的总积分是多少。
        """
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        # Declare our array along with base cases
        max_points = [0] * (max_number + 1)
        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            # Apply recurrence relation
            # 两种case，当前数被选，和当前数不被选
            max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num])

        return max_points[max_number]


class Solution5:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Time O(n + k)
        Space O(1)
        同思路4，只是空间优化的版本，因为我们只需要前面两次状态，用两个指针记录即可。
        """
        points = {}
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] = points.get(num, 0) + num
            max_number = max(max_number, num)

        # Base cases
        two_back = 0
        one_back = points.get(1, 0)

        for num in range(2, max_number + 1):
            two_back, one_back = one_back, max(one_back, two_back + points.get(num, 0))

        return one_back


class Solution6:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        思路和上面两个是一样的，只是这里不从最大值开始loop，直接loop所有存在的数，但是需要sort一下先，保证从小到大的顺序遍历。
        当前思路可能更快，因为有一种特殊情况，ex: 如果数组里面的只有三个数 [1, 2, 2^10]此时从最大值遍历需要遍历很多没必要的数，如果从出现
        的数的角度进行遍历，即使是sort，也不需要太费时。也就是要判断一下这个不等式 max_number < n + n * log(n, 2)。
        """
        points = defaultdict(int)
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num

        elements = sorted(points.keys())
        two_back = 0
        one_back = points[elements[0]]

        for i in range(1, len(elements)):
            current_element = elements[i]
            if current_element == elements[i - 1] + 1:
                # The 2 elements are adjacent, cannot take both - apply normal recurrence
                two_back, one_back = one_back, max(one_back, two_back + points[current_element])
            else:
                # Otherwise, we don't need to worry about adjacent deletions
                two_back, one_back = one_back, one_back + points[current_element]

        return one_back


s = Solution6()
print(s.deleteAndEarn(nums=[3, 4, 2]))
print(s.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
