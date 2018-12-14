class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,4]))