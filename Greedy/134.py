class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        """
        time: O(n), space: O(1)
        「那么局部最优：当前累加rest[j]的和curSum一旦小于0，起始位置至少要是j+1，因为从j开始一定不行。全局最优：找到可以跑一圈的起始位置」
        此题巧妙在能否跑完算总的每一个的差值，在假如可以跑完的情况下，我们已经差值为正数的作为开始位置，并且这个位置之后的所有差值都不能小于零
        :param gas:
        :param cost:
        :return:
        """
        cur_sum = 0
        total_sum = 0
        start = 0
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum < 0:                 # 当前累加rest[i]和 curSum一旦小于0
                start = i + 1               # 起始位置更新为i+1
                cur_sum = 0                 # curSum从0开始

        if total_sum < 0:                   # 走不完一圈，总和永远是负数
            return -1

        return start


s = Solution()
print(s.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
