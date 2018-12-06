class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        previous = 0
        current = 0
        sums = 0
        for letter in s:
            current = roman_dict[letter]
            sums += current
            if current > previous:
                sums -= 2 * previous
            previous = current

        return sums


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
