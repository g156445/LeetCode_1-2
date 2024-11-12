'''
题目要求我们找到数组 nums 中满足“好数组”条件的最长子数组的长度
让我们逐步解释一下关键点：
    频率：给定一个元素 x，它的频率是它在数组 nums 中出现的次数。比如，若 nums = [1, 2, 2, 3]，那么元素 2 的频率为 2
    好数组：一个数组被称为好数组，当它的所有元素的频率都小于等于 k。就是说，数组中每个元素的出现次数不能超过 k
    任务：题目要求找到 nums 中最长的子数组（即数组的一个连续部分），使得这个子数组是“好数组”，并返回这个子数组的长度
'''

class Solution:
    def maxSubarrayLength(self, nums, k):