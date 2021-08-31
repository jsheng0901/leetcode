class Solution:
    def maximumUnits(self, boxTypes: [[int]], truckSize: int) -> int:
        """
        O(nlog(n)) time, sort used nlog(n) + loop used n == O(nlog(n)), space O(1) 
        其实此题也可以看做贪心，需要整体最大，则每次先选取局部box unit最大的添加，然后从大到小添加直到达到size
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)     # sort decreasing by unit number

        res = 0

        for i in range(len(boxTypes)):
            if boxTypes[i][0] <= truckSize:         # if truck size bigger than box, then all add in
                res += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                res += truckSize * boxTypes[i][1]       # if no more enough for all box, then just fill all and break
                break

        return res



