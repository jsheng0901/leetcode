class Solution:
    def partitionLabels(self, s: str) -> [int]:
        """
        Time: O(n)
        Space: O(1)
        在遍历的过程中相当于是要找每一个字母的边界，如果找到之前遍历过的所有字母的最远边界，说明这个边界就是分割点了
        """
        index_map = {}  # 记录所有字母出现的最远距离的index
        for i in range(len(s)):
            index_map[s[i]] = i

        right = 0
        left = 0
        result = []

        for j in range(len(s)):
            right = max(right, index_map[s[j]])  # 记录此时最远的右边的index

            if j == right:  # 当遇到最远index和当时index相等时候，则说明需要划分区间
                result.append(right - left + 1)  # 记录区间长度
                left = j + 1  # 更新左边的index到新的区间起点

        return result


s = Solution()
print(s.partitionLabels(s="ababcbacadefegdehijhklij"))
