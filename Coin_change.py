class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
       t=[float('inf')]*(amount+1)
       t[0]=0
       
       for coin in coins:

           for j in range(coin,amount+1):
               t[j]=min(t[j],1+t[j-coin])
       return -1 if t[amount]==float('inf') else t[amount]
    
        
coins = [1, 2, 5]
amount = 11

sol = Solution()

result = sol.coinChange(coins, amount)

print(result)