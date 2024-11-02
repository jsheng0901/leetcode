import bisect
from collections import defaultdict


class Solution1:
    def is_subsequence(self, source, string):
        # 双指针判断string是否是source的substring
        p1 = 0
        p2 = 0

        while p1 < len(source) and p2 < len(string):
            if source[p1] != string[p2]:
                p1 += 1
            else:
                p1 += 1
                p2 += 1

        return p2 == len(string)

    def shortestWay(self, source: str, target: str) -> int:
        """
        Time O(t * s)
        Space O(1)
        双指针贪心思路，逐一遍历target里面的字符，如果当前的substring是source里面的substring，那么继续叠加，如果不是说明我们需要，
        重新的一次组合。这里判断一个string是不是另一个的substring，双指针判断法。
        """
        # 转化成set，方便快速查是否存在
        source_chars = set(source)
        # 记录次数，初始化至少1次
        ans = 1
        # 记录当前target的substring
        tmp = ""
        i = 0

        while i < len(target):
            # 如果不存在，说明一定不行，直接返回
            if target[i] not in source_chars:
                return -1

            # 叠加substring
            tmp += target[i]

            # 判断是否是source的substring
            if self.is_subsequence(source, tmp) is False:
                # 如果不是，说明需要新的组合
                tmp = ""
                # 计数器 +1
                ans += 1
            # 如果是，说明可以继续叠加
            else:
                i += 1

        return ans


class Solution2:
    def shortestWay(self, source: str, target: str) -> int:
        """
        Time O(t + t * log(s))
        Space O(s)
        整体思路和思路1是一样的，但是我们这里同时用一个指针在source里面找相对位置，比如当前target里面的字符x在source里面对应的index是1，
        此时下一个z在source里面的对应的index应该大于1，如果存在说明一定有这个substring在source里面，如果不存在这个大于1的index，
        说明需要重新一个组合。这里对应一个字符所有出现的index里面，找第一个大于source指针的index，明显可以用二分法左边界写法找。
        """
        # List of indices for all characters in source
        char_to_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_to_indices[c].append(i)

        # Pointer for source
        source_iterator = 0

        # Number of times we need to iterate through source
        count = 1

        # Find all characters of target in source
        for char in target:

            # If character is not in source, return -1
            if char not in char_to_indices:
                return -1

            # Binary Search to find the index of the character in source
            # next or equal to the current source_iterator
            index = bisect.bisect_left(char_to_indices[char], source_iterator)

            # If we have reached the end of the list, we need to iterate
            # through source again, hence first index of character in source.
            # 说明需要再一个组合
            if index == len(char_to_indices[char]):
                count += 1
                # source指针的起点一定是当前字符的第一个index的下一个
                source_iterator = char_to_indices[char][0] + 1
            else:
                # source指针是当前找到index的下一个
                source_iterator = char_to_indices[char][index] + 1

        # Return the number of times we need to iterate through source
        return count


s = Solution2()
print(s.shortestWay(source="xyz", target="xzyxz"))
