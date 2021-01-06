def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        >>> dynammic programming
        
        The key trick is to transform the question into a knapsack
        question. Having the smallest weights is equivalent to dividing
        the rocks into two groups and minimize the difference of their sum.
        So the question is:
            - How do we find a subarry with the sum not greater
            than sum(stones) // 2
        
        This is exactly a 0-1 knapsack problem.
        """
        target = sum(stones)//2+1
        dp = [0] * target
        
        for i in range(len(stones)):
            for c in range(len(dp)-1, -1, -1):
                if stones[i] > c:
                    continue
                dp[c] = max(dp[c-stones[i]]+stones[i], dp[c])
        
        return sum(stones)-2*dp[-1]
