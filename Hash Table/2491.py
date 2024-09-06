from typing import List
from collections import defaultdict, Counter


class Solution1:
    def create_teams(self, skill, target):
        # two sum的思路，记录每个数出现的频率即可
        teams = []
        freq = defaultdict(int)
        for i in range(len(skill)):
            # 需要找的另一个数的值
            rest = target - skill[i]
            # 如果存在并且频率大于0
            if freq[rest] > 0:
                # 找到一个合理的组
                teams.append([skill[i], rest])
                # 相对应的减少一次使用频率
                freq[rest] -= 1
            # 如果不存在，先记录下来出现频率
            else:
                freq[skill[i]] += 1

        return teams

    def dividePlayers(self, skill: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        先找到每个team的值，然后利用two sum的思路，找到所有的组合，之后在遍历一次所有组合找到乘积之和。
        """
        # 判断一下是否可以正好被分组
        if len(skill) % 2 != 0:
            return -1

        # 计算有多少个组
        total_sum = sum(skill)
        number_teams = int(len(skill) / 2)

        # 判断一下每个组是否刚好可以被整分
        if total_sum % number_teams != 0:
            return -1

        # 每个组的技能值和
        each_team_sum_skill = int(total_sum / number_teams)

        # 构建每个组
        teams = self.create_teams(skill, each_team_sum_skill)

        # 如果不等于总共组的个数，说明不合理，返回 -1
        if len(teams) != number_teams:
            return -1

        # 计算最终每个组的乘积和
        res = 0
        for team in teams:
            res += team[0] * team[1]

        return res


class Solution2:

    def dividePlayers(self, skill: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        一模一样的思路1，只是我们并不需要记录每个组具体是什么，可以直接找到合理的组的时候就计算乘积。
        """
        # 同思路1
        if len(skill) % 2 != 0:
            return -1

        total_sum = sum(skill)
        number_teams = int(len(skill) / 2)

        if total_sum % number_teams != 0:
            return -1

        each_team_sum_skill = int(total_sum / number_teams)

        res = 0
        freq = defaultdict(int)
        # 记录有多少个找到合理的组
        count = 0
        for i in range(len(skill)):
            rest = each_team_sum_skill - skill[i]
            # 区别在这里
            if freq[rest] > 0:
                # 直接计算乘积
                res += skill[i] * rest
                # 计数器 +1
                count += 1
                freq[rest] -= 1
            else:
                freq[skill[i]] += 1

        # 如果找到合理的组的个数不等于一开始的设定，说明无法组成最终结果，返回 -1，否则返回结果
        return -1 if count != number_teams else res


class Solution3:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        其实还可以更快，我们直接计算所有数出现的频率，一个数出现的频率必须和对于组成target值的另一个数的出现频率一致，不然就会有无法成组的数，
        计算乘积也不需要每个变量，可以直接找到符合要求的组的数和频率，直接 x * y * freq 得到结果。
        """
        if len(skill) % 2 != 0:
            return -1

        total_sum = sum(skill)
        number_teams = int(len(skill) / 2)

        if total_sum % number_teams != 0:
            return -1

        each_team_sum_skill = int(total_sum / number_teams)

        res = 0
        freq = Counter(skill)
        # 区别在这里
        for k, v in freq.items():
            rest = each_team_sum_skill - k
            # 如果当前数出现频率和互补的另一个数出现频率不一样，说明无法满足题意，直接返回 -1
            if v != freq[rest]:
                return -1

            # 如果一样的频率，直接计算这一组数的乘积和
            res += k * rest * v

        # 最终要除以2，因为同样地组合我们会计算两次
        return res // 2


s = Solution3()
print(s.dividePlayers(skill=[2, 3, 4, 2, 5, 5]))
