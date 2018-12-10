#   旋转数组:给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。要求使用空间复杂度为 O(1) 的原地算法。
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 法1
        # later_list = nums[-k:]
        # front_list = nums[:-k]
        # nums[:] = later_list + front_list
        # print(nums)

        # 法2
        # i = 0
        # while i < k:
        #     n = nums.pop(-1)
        #     nums.insert(0, n)
        #     i += 1

        # 法3
        length = k % len(nums)
        nums[:] = nums[-length:] + nums[: -length]
        print(nums)





if __name__ == "__main__":
    s = Solution()
    s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
