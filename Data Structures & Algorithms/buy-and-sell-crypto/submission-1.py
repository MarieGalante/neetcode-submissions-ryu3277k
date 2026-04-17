class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #brute force
        # for each start point, what is the maximum difference for every end point
        # bestdiff = 0
        # for i in range(len(prices)-1):

        #     for j in range(i+1, len(prices)):
        #         diff = prices[j] - prices[i]
                
        #         if diff>bestdiff:
        #             bestdiff = diff
        # return bestdiff

        # dynamic programming
        # find max of last 2, then last 3 versus tha last 2

        prefixmin_ls = [0]*len(prices)
        prefixmin_ls[0] = prices[0]
        for i in range(1, len(prices)):
            prefixmin_ls[i] = min(prefixmin_ls[i-1], prices[i-1])

        bestdif  = 0
        for i in range(1, len(prices)):
            diff = prices[i]  - prefixmin_ls[i]
            if diff > bestdif:
                bestdif = diff
        # print(prefixmin_ls)
        return bestdif
        