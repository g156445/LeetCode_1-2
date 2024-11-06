# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度

class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        char_map = {}  # 将每个字母拆开放到字典里，并记录位置
        max_len = 0

        for right in range(len(s)):
            # 假设右边有重复的
            # 如果窗口右边向右移1位，不存在在字典里；并且窗口左边划过的字母大于左边窗口（因为当右边窗口出现之前窗口以前的字母时，会报错）
            '''
            假设字符串s = "abba"
                1. 遍历到第一个 a（right = 0），无重复，记录位置 char_map["a"] = 0
                2. 遍历到第一个 b（right = 1），无重复，记录位置 char_map["b"] = 1
                3. 遍历到第二个 b（right = 2），发现 b 已经在 char_map 中，且 char_map["b"] = 1 >= left = 0，所以在当前窗口内有重复字符 b。我们将 left 更新为 char_map["b"] + 1 = 2
                4. 遍历到第二个 a（right = 3），此时 char_map["a"] = 0，但 0 < left = 2，表示上一次的 a 不在当前窗口内，因此 a 不影响当前窗口的无重复性
            '''
            if s[right] in char_map and char_map[s[right]] >= left:
                # 更新左边界到重复字符的下一位
                left = char_map[s[right]] + 1

            # 更新当前字符的位置
            char_map[s[right]] = right
            max_len = max(max_len, len(s[left:right+1]))

        return max_len


solution = Solution()

s = "abcbf"
print(solution.lengthOfLongestSubstring(s))

# s = "abcabcbb"
# char_map = {}
# char_map[s[2]] = 1
# print(char_map)
