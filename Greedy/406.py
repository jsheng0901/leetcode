import functools


class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        """
        time: O(nlogn + n^3), space: O(n)
        数组的插入操作复杂度是O(n^2)：寻找插入元素位置O(1)，插入元素O(n^2)，因为插入元素后面的元素要整体向后移。n个数所以是n^3
        我们就是要模拟一个插入队列的行为，所以不应该使用数组，而是要使用链表！

        遇到两个维度权衡的时候，一定要先确定一个维度，再确定另一个维度。
        此题用h先排序，这样按身高高度从大到小先确定，同身高，K小的在前面，
        按照身高排序之后，优先按身高高的people的k来插入，后序插入节点也不会影响前面已经插入的节点，最终按照k的规则完成了队列。

        「局部最优：优先按身高高的people的k来插入。插入操作过后的people满足队列属性」
「       全局最优：最后都做完插入操作，整个队列满足题目队列属性」
        :param people:
        :return:
        """

        def cmp(item1, item2):
            if item1[0] == item2[0]:
                if item1[1] < item2[1]:
                    return -1
                else:
                    return 1
            else:
                if item1[0] < item2[0]:
                    return 1
                else:
                    return -1

        people.sort(key=functools.cmp_to_key(cmp))

        # 比较慢的写法用list，python貌似没法写linked list链表来return list
        queue = []
        for i in range(len(people)):
            position = people[i][1]
            queue.insert(position, people[i])

        return queue


s = Solution()
print(s.reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
