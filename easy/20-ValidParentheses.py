class Solution:
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#' 
                if mapping[char] != top_element:
                    return False
            elif char in mapping.values():
                stack.append(char)
            
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.is_valid("{[]}"))
