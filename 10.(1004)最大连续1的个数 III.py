'''
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

    示例 1：
    输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    输出：6
    解释：[1,1,1,0,0,1,1,1,1,1,1]
    粗体数字从 0 翻转到 1，最长的子数组长度为 6。

    示例 2：
    输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    输出：10
    解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    粗体数字从 0 翻转到 1，最长的子数组长度为 10。
'''


class Solution:
    def longestOnes(self, nums, k):
        store_k = []  # 记录窗口内 0 的位置
        left = 0      # 窗口的左边界
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                store_k.append(right)  # 记录当前 0 的位置

            # 如果翻转的 0 超过了 k 个，调整左边界
            if len(store_k) > k:
                # 窗口左边界移动到 store_k 中最早的 0 的右侧
                left = store_k.pop(0) + 1

            # 更新最大长度
            max_length = max(max_length, right - left + 1)

        return max_length

# 测试
solution = Solution()
print(solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 输出：6
print(solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # 输出：10






