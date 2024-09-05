class Solution:
    def arrangeWords(self, text: str) -> str:
        """
        Time O(n)
        Space O(n)
        此题很直接了，先把所有变成小写，然后split开，sort通过单词长度，Python build-in 的sort本身会考虑original index当长度一样的时候，
        然后再拼接回来所有的word，最后再把首字母变成大写。
        """
        # 小写所有字符
        text = text.lower()
        # split开所有的单词
        text_list = text.split()
        # 通过长度排序
        text_list_sorted = sorted(text_list, key=lambda x: len(x))
        # 拼接回来所有的单词
        sorted_text = " ".join(text_list_sorted)
        # 返回首字母大写的结果
        return sorted_text.capitalize()


s = Solution()
print(s.arrangeWords(text="Leetcode is cool"))
print(s.arrangeWords(text="Keep calm and code on"))
print(s.arrangeWords(text="To be or not to be"))
