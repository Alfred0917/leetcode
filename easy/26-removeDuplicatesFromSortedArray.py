class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            index = 0
            for i in nums:
                if nums[index] != i:
                    index += 1
                    nums[index] = i
            print(nums)
            return index+1
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([],))
