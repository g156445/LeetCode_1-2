'''
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用
如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1
'''

class Solution:
    def minOperations(self, nums, x):