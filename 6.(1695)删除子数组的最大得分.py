'''
找到一个正整数数组 nums 中的最大得分子数组，条件是这个子数组中的元素都必须是不同的
题目的具体要求是：
    你可以删除数组 nums 中的一个子数组，得到的得分是该子数组的所有元素之和
    你的目标是找到只删除一个子数组，能够得到的最大得分

示例 1：
    输入：nums = [4, 2, 4, 5, 6]
    输出：17
    解释：包含不同元素的最优子数组是 [2, 4, 5, 6]，它的和是 2 + 4 + 5 + 6 = 17

示例 2：
    输入：nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    输出：8
    解释：包含不同元素的最优子数组可以是 [5, 2, 1] 或 [1, 2, 5]，它们的和都是 8
'''

class Solution:
    def maximumUniqueSubarray(self, nums):
        # 滑动窗口起点
        left = 0
        # 用于记录窗口中的元素
        seen = set()
        # 当前窗口的总和
        current_sum = 0
        # 最大得分
        max_sum = 0

        for right in range(len(nums)):
            # 如果当前元素已经在窗口中，调整窗口左边界直到移除重复的元素
            while nums[right] in seen:
                seen.remove(nums[left])  # 从集合中移除左边元素
                current_sum -= nums[left]  # 更新当前窗口的和
                left += 1  # 左边界右移

            # 将当前元素加入窗口
            seen.add(nums[right])
            current_sum += nums[right]

            # 更新最大得分
            max_sum = max(max_sum, current_sum)

        return max_sum

# 测试代码
solution = Solution()
print(solution.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))  # 输出 8
print(solution.maximumUniqueSubarray([4, 2, 4, 5, 6]))  # 输出 17
