class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        letter_list = []
        for letters in zip(*strs):
            if len(set(letters)) == 1:
                letter_list.append(letters[0])
            else:
                break

        return ''.join(letter_list)


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
