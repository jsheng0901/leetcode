from collections import defaultdict


class Solution1:
    def check_permutation(self, need, s2):
        # 判断是不是排列，此处不能对need字典进行修改，因为need是全局参数，如果修改后会影响后续再一次使用
        # 只能统计子串的出现次数，然后判断是否字符相同并且是否次数相等
        window = defaultdict(int)
        for c in s2:
            window[c] += 1

        # 判断出现此次和是否出现
        for k, v in need.items():
            if k not in window:
                return False
            elif window[k] != v:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time O(n * len(s1))
        Space O(n)
        单一指针，每次遇到符合情况的字符，提取等长的子串，然后判断是否是排列的情况，时间复杂度高于双指针，因为需要多次判断是不是排列。
        """
        # 构建字典，记录字符需要出现的次数
        need = defaultdict(int)

        for c in s1:
            need[c] += 1

        p = 0

        while p < len(s2):
            c = s2[p]
            # 如果该字符在需要的字典里，提取等长的子串
            if c in need:
                sub_s2 = s2[p: p + len(s1)]
                # 判断是否是排列，是则直接返回，不是则继续
                if self.check_permutation(need, sub_s2):
                    return True
            p += 1

        return False


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time O(n)
        Space O(n)
        滑动窗口模板题目，和76不一样的是每次维护的是一个定长窗口也就是一个length等于s1的窗口，所以窗口内只要字符串出现的次数满足，则一定是
        排列情况，不会出现子串的情况。
        """
        # 创建字典，记录字符需要出现的次数
        window = defaultdict(int)
        need = defaultdict(int)

        for c in s1:
            need[c] += 1

        left, right = 0, 0
        valid = 0

        # 右指针前移，更新窗口内数据
        while right < len(s2):
            c = s2[right]
            right += 1
            # 如果该字符在需要的字典里，更新窗口内字典
            if c in need:
                window[c] += 1
                # 如果窗口内字典该字符准确次数与需要的次数相同，计数器+1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否需要收缩
            while right - left >= len(s1):
                # 如果子串合法，返回True
                if valid == len(need):
                    return True
                # 左指针前移了，需要从窗口内字典中减掉一个元素
                d = s2[left]
                left += 1
                if d in need:
                    # 如果窗口内字典该字符准确次数与需要的次数相同，计数器-1
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        # 未找到合法的子串，返回False
        return False
