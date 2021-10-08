from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        value = self.cache[key]
        self.cache.pop(key)  # remove the key first
        self.cache[key] = value  # add this key to end of orderedDict
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache.keys()) == self.capacity:
                self.cache.popitem(last=False)  # always pop first item in orderedDict

            self.cache[key] = value

# TODO: use double link list and dict to implement orderedDict

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)