# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度
import string


class Solution:
    def lengthOfLongestSubstring(self, s):
        step = len(s)
        before = s[0]
        last = s[1]
        for location in range(step-1):
            if before != last:
                last =
                sub_string = s[before:last+1]
            # if before == last:
            #     sub_string = s[before+1:last]
        return sub_string

solution = Solution()

s = "abcdf"
print(solution.lengthOfLongestSubstring(s))
