class Solution:
    def isValid(self, word: str) -> bool:
        """
        Time O(n)
        Space O(n)
        直接根据题意进行翻译，先检查是否有不合规的字符，还有长度，然后检查是否有至少一个元音和非元音字符存在。
        """
        # 检查不合规的字符是否存在
        imp = {'@', '#', '$'}
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        if len(word) < 3 or any(i in imp for i in word):
            return False

        # 检查元音和非元音是否存在
        consonant = set()
        v = set()
        for i in word:
            if i in vowel and i not in v:
                v.add(i)
            elif i.isalpha() and i not in vowel and i not in consonant:
                consonant.add(i)

        # 满足同时两个条件
        return len(v) > 0 and len(consonant) > 0


s = Solution()
print(s.isValid(word="234Adas"))
print(s.isValid(word="b3"))
print(s.isValid(word="a3$e"))
