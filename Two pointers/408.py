class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        O(n) time
        two pointers, keep two pointers loop, once find digit find all digit and record sum and str
        (check if it's start with 0), then let word jump by sum, keep check alpha if it's same,
        final check is two pointers both reach the end. 
        """
        i = 0
        j = 0
        num = 0
        s = ''

        while i < len(word) and j < len(abbr):
            while j < len(abbr) and abbr[j].isdigit():
                num = 10 * num + int(abbr[j])
                s += abbr[j]
                j += 1

            if len(s) > 0 and s[0] == str(0):
                return False
            else:
                i += num
                num = 0
                s = ''
            if j < len(abbr) and i < len(word) and abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return True if i == len(word) and j == len(abbr) else False




