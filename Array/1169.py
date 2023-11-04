from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        Time O(n^2)
        Space O(n)
        按照题意思进行翻译，需要注意的是，先判断是否有不成对的invalid交易，再判断单一的invalid交易，不然会错过一种情况，
        就是单一amount超过为invalid交易，同时之前也有配对不成功的invalid交易，而配对这个会被漏掉，如果不先判断配对的话。详细见注释
        """
        # 记录结果，人名到交易细节的hash map，同时记录交易的index
        res = []
        name_to_trans = {}
        # 用来记录check过的不合理index，避免出现重复交易加入结果
        invalid_set_index = set()
        for i in range(len(transactions)):
            # 当前交易
            trans = transactions[i].split(',')
            # 如果同一个人之前出现过
            if trans[0] in name_to_trans:
                # 判断之前出现过的所有交易
                value = name_to_trans[trans[0]]
                for v in value:
                    # 如果有不符合的加入结果，同时记录进 invalid_set_index
                    if v[3] != trans[3] and abs(int(v[1]) - int(trans[1])) <= 60:
                        # check是否之前记录过
                        if i not in invalid_set_index:
                            res.append(",".join(trans))
                            invalid_set_index.add(i)
                        # 之前记录的交易index用来查重
                        if v[0] not in invalid_set_index:
                            res.append(",".join([trans[0]] + v[1:]))
                            invalid_set_index.add(v[0])
                # 如果之前出现的都没有不符合，进行单一判断，判断是否超额
                if int(trans[2]) > 1000:
                    # 同样check是否记录过
                    if i not in invalid_set_index:
                        res.append(",".join(trans))
                        invalid_set_index.add(i)
                # 更新记录此次交易进同人名字下的 hash map，记录交易细节和当前交易index
                name_to_trans[trans[0]].append([i, trans[1], trans[2], trans[3]])
            else:
                # 如果没有出现过，则直接判断单笔交易是否超额
                if int(trans[2]) > 1000:
                    # 由于没有出现过，所以不需要查重判断，直接加入结果
                    res.append(",".join(trans))
                    invalid_set_index.add(i)
                # 创建新的人名和交易细节进 hash map
                name_to_trans[trans[0]] = [[i, trans[1], trans[2], trans[3]]]

        return res


s = Solution()
print(s.invalidTransactions(transactions=["alice,20,800,mtv", "alice,50,1200,mtv"]))
print(s.invalidTransactions(transactions=["bob,689,1910,barcelona", "alex,696,122,bangkok", "bob,832,1726,barcelona",
                                          "bob,820,596,bangkok", "chalicefy,217,669,barcelona",
                                          "bob,175,221,amsterdam"]))
print(s.invalidTransactions(
    transactions=["alice,20,800,mtv", "bob,50,1200,mtv", "alice,20,800,mtv", "alice,50,1200,mtv", "alice,20,800,mtv",
                  "alice,50,100,beijing"]))
print(s.invalidTransactions(
    transactions=["bob,627,1973,amsterdam", "alex,387,885,bangkok", "alex,355,1029,barcelona", "alex,587,402,bangkok",
                  "chalicefy,973,830,barcelona", "alex,932,86,bangkok", "bob,188,989,amsterdam"]))
