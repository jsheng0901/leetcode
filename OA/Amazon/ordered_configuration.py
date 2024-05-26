# 2024-05-01
from typing import List


# A barcode scanner can be configured by scanning a series of barcodes in the correct order. Barcode configurations
# are encoded into a single string and stored as a blob in the backend system. The client requests the configuration
# from the backend configuration service, and then needs to present the configurations in the correct order. The
# encoded configuration string is a series of <ordinal-index>/<configuration> pairs separated by '|'. The ordinal
# index value is a 4 digit numeric prefix within zeros. For example, the first configuration will be represented as
# 0001.
#
# The goals are to 1) validate the configuration string and 2) provide the configuration client the configuration
# values in the order required to successfully configure the barcode scanner.
#
# Validation conditions
#
# All configurations must be separated by a '|' character. Configurations cannot skip a number in the ordering; if
# there are three configuration strings, there must be a 1, 2, and 3 index. Configuration values are alphanumeric and
# may contain no other characters. Ordinal indices may not repeat; for example there cannot be two occurrences of the
# number "11". Each configuration value is unique, configurations do not repeat. The configuration ordinal index
# configurations cannot skip a value. If a configuration string is not valid, return ["Invalid configuration"].
#
# Function Description
#
# Complete the function orderedConfiguration in the editor.
#
# orderedConfiguration has the following parameters:
#
# str configuration: the encoded configuration string
# Returns
#
# str configuration[]: an array of configurations in the correct order


class Solution:
    def orderedConfiguration(self, configuration: str) -> List[str]:
        """
        Time O(n)
        Space O(n)
        先把每个code提取出来，按照index为key的方式存储起来，如果出现重复或者index超过总长度，直接返回不合理的string，否则存起来。
        最后按照顺序遍历整个长度，逐一添加进数组结果。
        """
        # split开先
        configuration_list = configuration.split('|')
        n = len(configuration_list)
        index_2_config = {}
        # 存储index对code的map
        for config in configuration_list:
            index = config[3]
            # 如果之前有重复的index或者超过总长度，返回不合理string
            if index in index_2_config or int(index) > n:
                return ["Invalid configuration"]
            # 存起来
            else:
                index_2_config[index] = config

        # 按照顺序逐一添加加入结果
        res = []
        for i in range(n):
            res.append(index_2_config[str(i + 1)][4:])

        return res


s = Solution()
print(s.orderedConfiguration("0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C"))
print(s.orderedConfiguration("000533B8XLD2EZ|0001DJ2M2JBZZR|0002Y9YK0A7MYO|0004IKDJCAPG5Q|0003IBHMH59SBO"))
print(s.orderedConfiguration("0002f7c22e7904|000176a3a4d214|000305d29f4a4b"))
print(s.orderedConfiguration("0002f7c22e7904|000176a3a4d214|000205d29f4a4b"))
