


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.memo = {}
        self.coins = coins
        return self.dp(amount)

    def dp(self, amount):
        if amount < 0:
            return float('inf')
        elif amount == 0:
            return 0
        elif amount in self.memo:
            return self.memo[amount]

        answer = float('inf')
        for coin in self.coins:
            answer = min(answer, 1 + self.dp(amount - coin))

        self.memo[amount] = answer

        return answer

coins = [1,2,5]
solution = Solution()
print(solution.coinChange(coins, 11))




