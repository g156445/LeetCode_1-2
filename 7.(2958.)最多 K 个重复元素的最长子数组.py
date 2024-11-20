'''
题目要求我们找到数组 nums 中满足“好数组”条件的最长子数组的长度
让我们逐步解释一下关键点：
    频率：给定一个元素 x，它的频率是它在数组 nums 中出现的次数。比如，若 nums = [1, 2, 2, 3]，那么元素 2 的频率为 2
    好数组：一个数组被称为好数组，当它的所有元素的频率都小于等于 k。就是说，数组中每个元素的出现次数不能超过 k
    任务：题目要求找到 nums 中最长的子数组（即数组的一个连续部分），使得这个子数组是“好数组”，并返回这个子数组的长度

示例 1：
    输入：nums = [1,2,3,1,2,3,1,2], k = 2
    输出：6
    解释：最长好子数组是 [1,2,3,1,2,3] ，值 1 ，2 和 3 在子数组中的频率都没有超过 k = 2 。[2,3,1,2,3,1] 和 [3,1,2,3,1,2] 也是好子数组。
    最长好子数组的长度为 6 。

示例 2：
    输入：nums = [1,2,1,2,1,2,1,2], k = 1
    输出：2
    解释：最长好子数组是 [1,2] ，值 1 和 2 在子数组中的频率都没有超过 k = 1 。[2,1] 也是好子数组。
    最长好子数组的长度为 2 。

示例 3：
    输入：nums = [5,5,5,5,5,5,5], k = 4
    输出：4
    解释：最长好子数组是 [5,5,5,5] ，值 5 在子数组中的频率没有超过 k = 4 。
    最长好子数组的长度为 4
'''


class Solution:
    def maxSubarrayLength(self, nums, k):
        # 初始化字典，用于记录每个数字的频率
        freq = {}
        # 双指针初始化
        left = 0
        # 用于记录最长子数组长度
        max_length = 0

        # 遍历数组，right 是右边界指针
        for right in range(len(nums)):
            # 更新频率字典
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # 如果当前数字的频率超过 k，调整左边界
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1  # 缩小窗口，左边界右移
                if freq[nums[left]] == 0:  # 如果频率为 0，从字典中删除
                    del freq[nums[left]]
                left += 1

            # 更新最长子数组长度
            max_length = max(max_length, right - left + 1)

        return max_length


# 测试用例
solution = Solution()
print(solution.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4))  # 输出: 4
print(solution.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))  # 输出: 6
print(solution.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1))  # 输出: 2




