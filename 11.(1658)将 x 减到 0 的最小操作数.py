'''
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用
如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1
'''

class Solution:
    def minOperations(nums, x):
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1  # 无法实现

        # 滑动窗口初始化
        start, current_sum = 0, 0
        max_length = -1

        # 遍历数组
        for end in range(len(nums)):
            current_sum += nums[end]  # 扩展窗口

            # 收缩窗口直到窗口内和不大于 target
            while current_sum > target and start <= end:
                current_sum -= nums[start]
                start += 1

            # 检查是否等于目标值
            if current_sum == target:
                max_length = max(max_length, end - start + 1)

        # 计算结果
        return len(nums) - max_length if max_length != -1 else -1

    # 测试用例
    print(minOperations([1, 1, 4, 2, 3], 5))  # 输出: 2
    print(minOperations([5, 6, 7, 8, 9], 4))  # 输出: -1
    print(minOperations([3, 2, 20, 1, 1, 3], 10))  # 输出: 5
