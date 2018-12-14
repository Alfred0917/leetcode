class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A, key=lambda x: x % 2)


if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))
