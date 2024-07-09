from typing import List


class Solution:
    def bfs(self, startGene, endGene, bank):
        """
        Time O(n)   n --> bank length
        Space O(n --> 8) --> O(1)
        因为这里bank的长度最大不过8，所以其实是否转换成set在check存在并不会影响太多，空间复杂度上因为是固定最大长度，所以基本上相当于是常数，
        基本的BFS思路，每次改变一个字符从候选字符中选择，判断是否在bank内或者是否访问过。注意每一步的改动都需要确保改动后的基因在bank内。
        """
        # BFS模版
        gene_string = ['A', 'C', 'G', 'T']
        path = set()
        path.add(startGene)
        queue = [(startGene, 0)]

        while queue:
            # 当前基因，注意Python要弹出队首
            cur_gene, cur_step = queue.pop(0)
            # 走到最后，直接返回当前step
            if cur_gene == endGene:
                return cur_step
            for i in range(len(cur_gene)):
                for string in gene_string:
                    # 下一个记忆
                    next_gene = cur_gene[:i] + string + cur_gene[i + 1:]
                    # 如果不在bank内直接跳过
                    if next_gene not in bank:
                        continue
                    # 如果访问过，跳过
                    if next_gene in path:
                        continue
                    # 合理的基因进入列队
                    queue.append((next_gene, cur_step + 1))
                    # 记录访问过
                    path.add(next_gene)

        return -1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        return self.bfs(startGene, endGene, bank)


s = Solution()
print(s.minMutation(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(s.minMutation(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))
