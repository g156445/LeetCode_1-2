class Solution:
    def maximumLengthSubstring(self, s):
        char_count = {}  # 记录窗口中每个字符的出现次数
        left = 0  # 窗口的左边界
        max_len = 0  # 记录满足条件的最长子串长度

        for right in range(len(s)):
            # 更新右边界字符的出现次数
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # 如果有字符出现次数超过两次，移动左边界
            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            # 更新最大长度
            max_len = max(max_len, right - left + 1)

        return max_len


# 测试代码
solution = Solution()
s = "bcbbbcba"
print(solution.maximumLengthSubstring(s))  # 输出应为 4
