def maxProfit(self, prices: List[int]) -> int:
        """
        >>> Dynammic Programming
        
        A state compression problem. We have three state:
            - sold
            - buy
            - cd
        to store the maximum profit ending with selling, buying and cooldown.
        And the next state is only determined by the last state.
        """
        buy, sold, cd = float('-inf'), float('-inf'), 0
        for p in prices:
            prev_buy = buy
            prev_sold = sold
            buy = max(cd-p, buy)
            sold = max(prev_buy+p, sold)
            cd = max(cd, prev_sold)
        
        return max(cd, sold)
