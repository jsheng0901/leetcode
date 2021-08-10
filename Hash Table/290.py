class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """每次loop每个pattern和word时候，如果不存在就同时存入一样的index，如果存在则检验对应的index是否相同，不同则false"""
        mapping = {}
        s_list = s.split(' ')
        if len(s_list) != len(pattern):
            return False

        for i in range(len(pattern)):
            c = 'char_{}'.format(pattern[i])        # 命名不一样的格式，因为会出现，pattern是a, 同时word也是a，则无法检验
            word = 'word_{}'.format(s_list[i])

            if c not in mapping:
                mapping[c] = i

            if word not in mapping:
                mapping[word] = i

            if mapping[c] != mapping[word]:
                return False

            # if pattern[i] not in mapping:
            #     if s_list[i] in mapping.values():
            #         return False
            #     else:
            #         mapping[pattern[i]] = s_list[i]
            # else:
            #     if mapping[pattern[i]] != s_list[i]:
            #         return False

        return True