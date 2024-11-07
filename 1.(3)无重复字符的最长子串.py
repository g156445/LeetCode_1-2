# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度

class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        char_map = {}
        max_len = 0

        for right in range(len(s)):
            '''
            假设字符串s = "abba"：
                1. 遍历到第一个 a（right = 0），无重复，记录位置 char_map["a"] = 0。
                2. 遍历到第一个 b（right = 1），无重复，记录位置 char_map["b"] = 1。
                3. 遍历到第二个 b（right = 2），发现 b 已经在 char_map 中，且 char_map["b"] = 1 >= left = 0，所以在当前窗口内有重复字符 b。我们将 left 更新为 char_map["b"] + 1 = 2。
                4. 遍历到第二个 a（right = 3），此时 char_map["a"] = 0，但 0 < left = 2，表示上一次的 a 不在当前窗口内，因此 a 不影响当前窗口的无重复性。
            '''
            if s[right] in char_map and char_map[s[right]] >= left:
                # 更新左边界到重复字符的下一位
                left = char_map[s[right]] + 1

            # 更新当前字符的位置
            char_map[s[right]] = right

            # 计算当前窗口长度并更新最大长度
            max_len = max(max_len, right - left + 1)

        return max_len

solution = Solution()
s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))