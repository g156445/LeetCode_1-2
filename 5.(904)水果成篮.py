class Solution:
    def totalFruit(self, fruits):
        fruit_dict = {}  # 用于记录窗口内每种水果的数量
        left = 0  # 滑动窗口的左边界
        max_sorts = 0  # 最大连续水果数

        for right, value in enumerate(fruits):
            # 将右边界的水果加入字典，并增加计数
            fruit_dict[value] = fruit_dict.get(value, 0) + 1

            # 如果窗口内的水果种类超过2种，缩小窗口
            while len(fruit_dict) > 2:
                fruit_dict[fruits[left]] -= 1
                # 如果某种水果的数量为0，则从字典中删除
                if fruit_dict[fruits[left]] == 0:
                    del fruit_dict[fruits[left]]
                # 移动左边界
                left += 1

            # 计算当前窗口内的最大水果数，并更新最大值
            max_sorts = max(max_sorts, right - left + 1)

        return max_sorts
