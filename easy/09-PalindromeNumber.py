class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            str_x = str(x)
            reverse_x = str_x[::-1]
            if str_x == reverse_x:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(0))
