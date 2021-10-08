class Solution:
    def nextDay(self, cells: [int]):
        ret = [0]  # head
        for i in range(1, len(cells) - 1):
            ret.append(int(cells[i - 1] == cells[i + 1]))
        ret.append(0)  # tail
        return ret

    def prisonAfterNDays(self, cells: [int], n: int) -> [int]:
        """
        O(k*min(n, 2^k)) time, O(k * 2^k) space
        find the loop cycle size, then jump to cycle end then applied next day simulation
        """
        seen = dict()
        is_fast_forwarded = False

        while n > 0:
            if not is_fast_forwarded:
                state = tuple(cells)
                if state in seen:
                    n %= seen[state] - n        # length of cycle is seen[state] - n
                    is_fast_forwarded = True
                else:
                    seen[state] = n

            if n > 0:
                n -= 1
                next_day = self.nextDay(cells)
                cells = next_day

        return cells



