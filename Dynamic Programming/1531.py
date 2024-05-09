class Solution:

    def dp(self, current_index, N, string, K_deletions, previous_character, current_frequency,
           dp_dictionary):

        # if the 'current_index' got exhausted return '0'

        if current_index == N:
            return 0

        # the variable values are 'current_index' , 'K_deletions' , 'previous_character' , 'current_frequency'

        # that's why it is used as 'key'

        key = (current_index, K_deletions, previous_character, current_frequency)

        # if the 'key' is already present in 'dp_dictionary' then return the 'value' stored in 'dp_dictionary[key]'

        if key in dp_dictionary:
            return dp_dictionary[key]

        # the 'increment_count' is initialized with '1' because the 'maximum string length is 100' and if the
        # frequency becomes a '2' digit number or if the 'current_frequency' is '1' then the next time during the
        # compression of the string it becomes '2' which should be counted for example , in string 'aa' the
        # 'current_frequency' is '1' and the next time when it compresses it becomes 'a2' the length is '2' right !
        # balance two conditions are nothing but handling the 'two digits frequency' for example , if the string is
        # 'aaaaaaaaaa' if the 'current_frequency' is '9' after compressing it becomes 'a10' see the compression
        # string length is now increased so only this condition is handled explicitly

        increment_count = 1 if (
                (current_frequency == 1) or (current_frequency == 9) or (current_frequency == 99)) else 0

        # typical binary cases !

        # 'pick' and 'not_pick'

        # The 'pick' has two scenarios ,

        # if the (string[current_index] == previous_character) means the same character's frequency is counted and
        # incremented along with the 'increment_count'

        # else 'new character' is encounter and the 'current_frequency' is reinitialized as '1' and '1' is added to
        # the 'pick' because the compression length of the 'new character' should start with '1'

        if string[current_index] == previous_character:
            pick = increment_count + self.dp(current_index + 1, N, string, K_deletions, previous_character,
                                             current_frequency + 1, dp_dictionary)
        else:
            pick = 1 + self.dp(current_index + 1, N, string, K_deletions, string[current_index], 1, dp_dictionary)

        # 'not_pick' has also two scenarios ,

        # 'if(K_deletions)' means that if the 'K_deletions' values is greater than '0' we have the possibility of
        # deleting this 'current_index' character

        # so the 'recursive_function' is called and the 'K_deletions' is decremented by '1' since we have deleted the
        # 'current_index' character

        # else we store the 'maximum_value' which is 'float('inf')' in 'not_pick' variable because we need the
        # 'minimum length'

        if K_deletions > 0:
            not_pick = self.dp(current_index + 1, N, string, K_deletions - 1, previous_character, current_frequency,
                               dp_dictionary)
        else:
            not_pick = float('inf')

        # finally storing the 'minimum value' in the 'dp_dictionary[key]'

        dp_dictionary[key] = min(pick, not_pick)

        # now return the 'value' stored in 'dp_dictionary[key]'

        return dp_dictionary[key]

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Time O(A * n^2 * k)    A --> number of previous character, n --> index or frequency, k --> number deletion
        Space O(A * n^2 * k)
        时间复杂度和空间复杂度可以看做dp数组的状态的乘积，此题很巧妙，核心思想应该是构建string，同时记录四种状态下的每一步最短的长度状态进dp。
        对于每个字符就两种选择，一个是pick这个数，另一个是不pick，具体的情况看注释。
        """
        return self.dp(0, len(s), s, k, '', 0, {})


s = Solution()
print(s.getLengthOfOptimalCompression(s="aaabcccd", k=2))
