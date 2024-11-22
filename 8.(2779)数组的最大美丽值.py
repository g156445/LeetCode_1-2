'''
在一定限制下，通过对数组元素的调整，来最大化数组的“美丽值”。

1. 输入参数：你有一个整数数组 `nums` 和一个非负整数 `k`。`nums` 是从下标 0 开始的数组。

2. 操作步骤：
   - 你可以在 `[0, nums.length - 1]` 范围内选择一个下标 `i`。
   - 选择的下标 `i` 之前没有被选择过（即每个元素最多只能被选一次）。
   - 选中元素 `nums[i]` 后，可以把它改成 `[nums[i] - k, nums[i] + k]` 范围内的任意一个整数。

3. 美丽值定义：
   - “美丽值” 是数组中相等元素组成的最长子序列的长度（即，某个数字连续出现的最大次数）。
   - 子序列可以通过删除一些元素得到（不影响顺序），但不一定要是连续的。

4. 目标：通过对 `nums` 中的每个元素进行上述操作，找出数组可能取得的最大美丽值。

### 理解要点

- 你需要思考如何修改数组中的元素，让相同的元素数量最多，这样可以增加“美丽值”。
- 操作限制为每个元素只能修改一次，所以需要合理安排哪些元素要变成什么值。

### 解题思路

1. 策略：为了增加美丽值，尽可能让更多元素变成相同的值。
2. 方法：遍历数组，确定某个目标值后，看看哪些元素可以通过操作变为这个值。
'''

class Solution:
    def maximumBeauty(self, nums, k):
        if not nums:  # 检查 nums 是否为空
            return 0

        record_time = {}
        for num in nums:
            left, right = num - k, num + k + 1

            for record in range(left, right):
                record_time[record] = record_time.get(record,0) + 1

            # 如果 record_time 为空，返回 0
            if not record_time:
                return 0

        most_common_value = max(record_time.values())
        return most_common_value
solution = Solution()
print(solution.maximumBeauty([4,6,1,2],2))

from typing import List

'''滑动窗口
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # 对数组排序
        nums.sort()

        left = 0  # 滑动窗口左指针
        max_beauty = 0  # 最大美丽值

        # 遍历数组，right 是滑动窗口的右指针
        for right in range(len(nums)):
            # 如果窗口中的最大值和最小值之差大于 2k，则缩小窗口
            while nums[right] - nums[left] > 2 * k:
                left += 1

            # 当前窗口长度就是可能的美丽值
            max_beauty = max(max_beauty, right - left + 1)

        return max_beauty
'''
