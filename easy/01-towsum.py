"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 1. 暴力法
        # result = {}
        # for i, j in enumerate(nums):
        #     if target - j in result:
        #         return [result[target-j], i]
        #     result[j] = i

        # 2. 一遍哈希表
        # lookup = {}
        # for i, item in enumerate(nums):
        #     if target-item in lookup:
        #         return [lookup[target-item], i]
        #     lookup[item] = i

        # 3. best ways
        dic = {}
        for i, w in enumerate(nums):

            if w in dic and dic[w] != i:
                return [dic[w], i]
            dic[target - w] = i


if __name__ == '__main__':
    result = Solution()
    print(result.twoSum([3, 3], 6))
    print(result.twoSum([3, 2, 4], 6))
