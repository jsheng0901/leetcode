import bisect


class Solution:
    def suggestedProducts(self, products: [str], searchWord: str) -> [[str]]:
        """
        O(nlog(n))+O(mlog(n)) time, first is sorting products, second is binary search product m times, O(1) or O(n)
        depends on sorting space and ignore output space
        binary search, first sorted products, then loop over search word, keep add prefix then for each prefix
        we find first index of product has this prefix in sorted products array, then add next 3 has same prefix
        """
        products.sort()
        res = []
        prefix = ''

        for ch in searchWord:
            temp = []
            prefix += ch
            index = bisect.bisect_left(products, prefix)        # find first product has same prefix binary search
            for product in products[index:]:
                if len(temp) >= 3 or product[:len(prefix)] > prefix:
                    break
                if product[:len(prefix)] == prefix:     # find next one if it's same prefix and add
                    temp.append(product)

            res.append(temp)

        return res


s = Solution()
print(s.suggestedProducts(["bags", "baggage", "banner", "box", "cloths"], "bags"))
