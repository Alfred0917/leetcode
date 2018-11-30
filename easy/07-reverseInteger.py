# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            newX = int(str(x)[::-1])

        else:
            newX = int(str(x)[0] + str(x)[1:][::-1])
        return newX if -2147483648 < newX < 2147483648 else 0


if __name__ == '__main__':
    result = Solution()
    print(result.reverse(432100))
    print(result.reverse(-532543500))
    print(result.reverse(9432759812093747213496237896498123674164976123984))
