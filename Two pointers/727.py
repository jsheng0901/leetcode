from collections import defaultdict


class Solution1:
    def id_subsequence(self, s1, s2):
        p1 = 0
        p2 = 0
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p2 += 1
            p1 += 1

        return p2 == len(s2)

    def minWindow(self, s1: str, s2: str) -> str:

        window = defaultdict(int)
        need = defaultdict(int)
        for c in s2:
            need[c] += 1

        left = 0
        right = 0
        length = float('inf')
        valid = 0
        res = ""

        while right < len(s1):
            c = s1[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need) and self.id_subsequence(s1[left: right], s2):
                if right - left < length:
                    res = s1[left: right]
                    length = right - left
                d = s1[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return res


class Solution2:
    def minWindow(self, s1: str, s2: str) -> str:

        window = defaultdict(int)
        need = defaultdict(int)
        for c in s2:
            need[c] += 1

        left = 0
        right = 0
        p1 = 0
        p2 = 0
        length = float('inf')
        valid = 0
        res = ""

        while right < len(s1):
            c = s1[right]
            if c in need:
                window[c] += 1
                if c == s2[p1]:
                    p1 += 1
                if window[c] == need[c]:
                    valid += 1
            right += 1

            while valid == len(need) and p1 == len(s2):
                p2 = 0
                if right - left < length:
                    res = s1[left: right]
                    length = right - left
                d = s1[left]
                if d in need:
                    if window[d] == need[d] and s1[left] == s2[p2]:
                        valid -= 1
                        p1 = 0
                    window[d] -= 1
                left += 1

        return res


s = Solution2()
print(s.minWindow(s1="ffynmlzesdshlvugsigobutgaetsnjlizvqjdpccdylclqcbghhixpjihxim"
                     "vhapymfkjxyyxfwvsfyctmhwmfjyjidnfryiyajmtakisaxwglwpqaxaicupr"
                     "rvxybzdxunypzofhpclqiybgniqzsdeqwrdsfjyfkgmejxfqjkmukvgygafwok"
                     "eoeglanevavyrpduigitmrimtaslzboauwbluvlfqquocxrzrbvvplsivujojscytm"
                     "eyjolvvyzwizpuhejsdzkfwgqdbwinkxqypaphktonqwwanapouqyjdbptqfowhemsnsl", s2="michmznait"))
print(s.minWindow(s1="abcdebdde", s2="bde"))
