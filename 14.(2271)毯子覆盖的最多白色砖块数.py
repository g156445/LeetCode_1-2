'''
给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。
同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子的长度。
请你返回使用这块毯子，最多 可以盖住多少块瓷砖。
'''


class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen):
