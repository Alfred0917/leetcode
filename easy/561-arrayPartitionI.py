class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted(nums)
        return sum(nums[::2])


if __name__ == "__main__":
    s = Solution()
    print(s.arrayPairSum([1, 4, 2, 2]))
