class Solution:
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if prices:
        #     if sorted(prices) == prices:
        #         # 正序
        #         return prices[-1] - prices[0]
        #     elif sorted(prices, reverse=False) == prices:
        #         # 逆序
        #         return 0
        #     else:
        #         # 乱序
        #         previous = prices[0]
        #         current = 0
        #         profit_list = []
        #         for price in prices[1:]:
        #             current = price
        #             if current > previous:
        #                 profit = current - previous
        #                 profit_list.append(profit)
        #             previous = current

        #         return sum(profit_list)

        # else:
        #     return 0
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                max_profit += prices[i] - prices[i-1]
        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([]))
