class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # new_A = []
        # for x in range(len(A[0])):
        #     inside_A = []
        #     for i, j in enumerate(A):
        #         inside_A.append(A[i][x])
        #     new_A.append(inside_A)

        # return new_A

        A = list(map(list, zip(*A)))
        return A


if __name__ == "__main__":
    s = Solution()
    print(s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
