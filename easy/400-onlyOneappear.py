class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                return i

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))