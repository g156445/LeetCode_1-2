# 1493. 删掉一个元素以后全为 1 的最长子数组

# 主要逻辑
#   1.不定长滑动窗口逻辑：
#       当窗口条件被破坏（即窗口内0的数量超过允许的1个）时，通过移动left指针收缩窗口，直到条件重新满足（窗口内0的数量为1）
#   2.右边界扩展：
#       每次右边界right移动时，根据count_zero的值判断是否需要收缩窗口
#   3.窗口长度更新：
#       当窗口条件满足时，计算当前窗口的有效长度（不包含一个需要“删除”的元素）


class Solution:
    def longestSubarray(self, nums):
        # 初始化左边界 left，窗口内的 0 的计数器 count_zero，以及最大长度 max_len
        left = 0
        count_zero = 0
        max_len = 0

        # 遍历数组，用 right 作为右边界
        for right in range(len(nums)):
            # 如果遇到 0，增加 count_zero，表示当前窗口内的 0 数量
            if nums[right] == 0:
                count_zero += 1

            # 不定长滑动窗口的核心逻辑：当窗口内有超过一个 0 时，移动左边界以缩小窗口
            while count_zero > 1:
                # 如果左边界是 0，减少 count_zero，因为左边界要右移
                if nums[left] == 0:
                    count_zero -= 1
                # 将左边界右移一位，缩小窗口，使得窗口内最多只有一个 0
                left += 1

            # 更新 max_len，记录当前窗口的最大长度
            # 注意这里是 right - left 而不是 right - left + 1，因为要“删掉”一个元素
            max_len = max(max_len, right - left)

        # 返回最长的且只包含 1 的非空子数组长度
        return max_len

