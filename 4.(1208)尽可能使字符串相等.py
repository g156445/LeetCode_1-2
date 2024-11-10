class Solution:
    def equalSubstring(self, s, t, maxCost):
        list_difference = []
        # 记录每个字符位置的差值
        for right in range(len(s)):
            char_difference = abs(ord(s[right]) - ord(t[right]))
            list_difference.append(char_difference)

        # 滑动窗口的左边界初始化
        left = 0
        # 当前窗口的总开销
        current_cost = 0
        # 最大可变换长度
        max_length = 0

        # 滑动窗口右边界从0到字符串长度
        for right in range(len(s)):
            # 增加当前右边界字符的开销
            current_cost += list_difference[right]

            # 如果当前开销超出最大预算，收缩左边界
            while current_cost > maxCost:
                current_cost -= list_difference[left]
                left += 1

            # 更新最大长度为当前窗口的长度
            max_length = max(max_length, right - left + 1)

        return max_length, list_difference


solution = Solution()
s = "abcd"
t = "bcdf"
maxCost = 3

print(solution.equalSubstring(s, t, maxCost))