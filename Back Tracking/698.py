from typing import List


class Solution1:
    def backtracking(self, nums, index, target, bucket):
        # 所有数都填完了，检查每个桶里的数字和都是不是 target
        if index == len(nums):
            # 如果有不是的桶，返回false
            for i in bucket:
                if i != target:
                    return False
            return True

        # 每个桶都尝试一下
        for i in range(len(bucket)):
            # 如果加进去这个数，这个桶的数字和就超过了 target，那就不能加了
            if bucket[i] + nums[index] > target:
                continue
            # 选择装进第 i 个桶
            bucket[i] += nums[index]
            # 如果这个加法是可行方案，就继续递归下去
            if self.backtracking(nums, index + 1, target, bucket):
                return True
            # 撤销选择，恢复现场，继续尝试别的加法
            bucket[i] -= nums[index]
        # 无解，返回 false
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        Time O(k^n)  n个数字，每个数字有k个选择
        Space O(n)
        时间复杂度来说两种solution最差情况虽然一样，但是其实第一种情况需要遍历的更多，并且不能用状态来减枝。
        这里从数字的角度来看，每个数字可以放进这个桶或者不放进。每个数字都要选择进入到 k 个桶中的某一个。
        """
        # 排除一些基本情况
        if k > len(nums):
            return False
        # 降序排序 nums 数组，让更大的数字先来装，达到减枝的作用
        nums.sort(reverse=True)
        # 将所有数的和求出来
        sum_nums = sum(nums)
        # 如果所有数的和不能被 k 整除，就不用继续了
        if sum_nums % k != 0:
            return False
        # 所有分出来的桶需要装 target 个数字
        target = sum_nums // k
        # k 个桶（集合），记录每个桶装的数字之和
        bucket = [0] * k

        # 穷举 nums 中的每个数字
        return self.backtracking(nums, 0, target, bucket)


class Solution2:
    def backtracking(self, k, nums, index, used, target, bucket, memo):
        # base case，如果桶用完则说明走到底了，返回true
        if k == 0:
            # 所有桶都被装满了，而且 nums 一定全部用完了
            # 因为 target == sum / k
            return True

        # 将 used 的状态转化成形如 [true, false, ...] 的字符串，便于存入 HashMap
        state = str(used)

        # 装满了当前桶，递归穷举下一个桶的选择
        if bucket == target:
            # 让下一个桶从 nums[0] 开始选数字
            res = self.backtracking(k - 1, nums, 0, used, target, 0, memo)
            # 将当前状态和结果存入备忘录
            memo[state] = res
            # 返回递归结果
            return res

        # 如果当前状态曾今计算过，就直接返回，不要再递归穷举了
        if state in memo:
            return memo[state]

        # 从 index 开始向后探查有效的 nums[i] 装入当前桶
        for i in range(index, len(nums)):
            # 剪枝，nums[i] 已经被装入别的桶中
            if used[i] is True:
                continue
            # 当前桶装不下 nums[i]
            if bucket + nums[i] > target:
                continue
            # 做选择，将 nums[i] 装入当前桶中
            used[i] = True
            bucket += nums[i]
            # 递归穷举下一个数字是否装入当前桶
            if self.backtracking(k, nums, i + 1, used, target, bucket, memo):
                # 如果是true，返回本层递归结果
                return True
            # 撤销选择
            used[i] = False
            bucket -= nums[i]

        # 穷举了所有数字，都无法装满当前桶
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        Time O(k*2^n) 每个桶要遍历 n 个数字，对每个数字有装入或不装入两种选择，所以组合的结果有 2^n 种，总共k个桶。
        Space O(n)
        基本思路，从桶的角度看问题，每个桶装满了目标值后进入下一个桶，每个桶需要从第一个数字开始一个一个尝试放进去，然后判断是否满足条件。
        这里用used数组记录当遍历下一个桶的时候前一个桶是否用过这个数字，把used数组转化成string来记录进备忘录，为了避免同一种状态下用过的数组
        情况在下一次桶的情况中重复使用，ex: 第一个桶 1 4，第二个桶 2 3。第二个桶 1 4，第一个桶 2 3。第二种情况起始和第一种情况是一模一样。
        这里两种情况的使用used状态是一样的都是true true true true，所以 used 数组可以认为是回溯过程中的「状态」。
        所以，我们可以用一个 memo 备忘录，在装满一个桶时记录当前 used 的状态，如果当前 used 的状态是曾经出现过的，那就不用再继续穷举，
        从而起到剪枝避免冗余计算的作用。
        两种solution对比效率得出，通俗来说，我们应该尽量「少量多次」，就是说宁可多做几次选择（乘法关系），也不要给太大的选择空间（指数关系）；
        做 n 次「k 选一」仅重复一次（O(k^n)），比 n 次「二选一」重复 k 次（O(k*2^n)）效率低很多。
        """
        # 排除一些基本情况
        if k > len(nums):
            return False

        sum_nums = sum(nums)

        if sum_nums % k != 0:
            return False

        # 先装大的数字，可以有效的达到如果桶中的和超过了target，早点减枝，早点结束递归。
        nums.sort(reverse=True)
        target = sum_nums // k
        used = [False] * len(nums)
        memo = {}

        # k 号桶初始什么都没装，从 nums[0] 开始做选择
        return self.backtracking(k, nums, 0, used, target, 0, memo)


s = Solution2()
print(s.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
