from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        O(l1 + (l2 - l1)) time, O(1) space
        记录s1的词频， 滑动窗口更新s2的词频，窗口size是s1的length，如果hash_map词频相等则return true
        """
        s1_counter = Counter(s1)
        left = 0
        right = len(s1) - 1
        s2_counter = Counter(s2[:right])

        while right < len(s2):
            s2_counter[s2[right]] += 1
            if s2_counter == s1_counter:
                return True
            s2_counter[s2[left]] -= 1

            if s2_counter[s2[left]] == 0:
                del s2_counter[s2[left]]

            left += 1
            right += 1

        return False


