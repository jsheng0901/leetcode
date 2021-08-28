class Solution:
    def reorderLogFiles(self, logs: [str]) -> [str]:
        """自定义sort用的key O( m * n * log(n)) time, m is max length of one string, n * log(n) sort time"""
        def get_key(log):
            id, content = log.split(' ', maxsplit=1)

            return (0, content, id) if content[0].isalpha() else (1,)   # will sort follow key in () one by one

        return sorted(logs, key=get_key)



