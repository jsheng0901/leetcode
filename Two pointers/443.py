from typing import List


class Solution1:
    def compress(self, chars: List[str]) -> int:
        """
        Time O(n)
        Space O(1)
        双指针写法，难点在于如何in-palace压缩list，其实很简单思路，找到一个连续的区间后，
        直接给指定长度的对应的index地方修改为当前的character，并且如果长度大于1的话就同时更新后续位置的长度。需要注意的是最后一个连续的区间
        需要额外在loop后操作，因为loop会跳出去。
        """
        # 特殊情况，直接返回1
        if len(chars) == 1:
            return 1

        # 记录长度
        res = 0
        # 双指针
        left = 0

        for right in range(len(chars)):
            # 如果当前指针和左指针不相等，说明找到一个连续的区间
            if chars[right] != chars[left]:
                # 首先更新当前结果对应的字符
                chars[res] = chars[left]
                # 计算长度
                count = right - left
                # 结果 +1，同时对应的index向前走一步
                res += 1
                # 如果大于1，需要加入长度
                if count > 1:
                    # 转化成string
                    str_count = str(count)
                    # 在插入字符后面直接加入长度
                    chars[res: res + len(str_count)] = list(str_count)
                    # 更新长度
                    res += len(str_count)
                # 左指针跳到找到不相等的字符的index
                left = right

        # 对最后一个连续区间操作，一样的逻辑
        last_count = len(chars) - left
        if last_count == 1:
            chars[res] = chars[left]
            res += 1
        else:
            chars[res] = chars[left]
            res += 1
            str_count = str(last_count)
            chars[res: res + len(str_count)] = list(str_count)
            res += len(str_count)

        return res


class Solution2:
    def compress(self, chars: List[str]) -> int:
        """
        Time O(n)
        Space O(1)
        单一指针写法，思路一模一样，但是这里计算连续区间的长度，不再需要额外处理最后一个连续区间。
        """
        i = 0
        res = 0
        while i < len(chars):
            # 区别在于这里先一直计算连续区间的长度
            group_length = 1
            while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
                group_length += 1
            # 对应index位置赋值字符
            chars[res] = chars[i]
            # 长度更新
            res += 1
            # 处理大于1的情况
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            # 更新指针的位置，等同于左指针跳到右指针的位置
            i += group_length

        return res


s = Solution2()
print(s.compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
print(s.compress(chars=["a"]))
print(s.compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
